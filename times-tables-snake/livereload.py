import os
import importlib

import pygame
from watchdog import observers, events

import snake


HERE = os.path.abspath(os.path.dirname(__file__))


def main():
    pygame.init()
    display = pygame.display.set_mode(snake.SCREEN_DIMENSIONS)

    path = os.path.join(HERE)    
    controller = snake.Controller()

    def start_game():
        controller.reset()

        importlib.reload(snake)
        snake.game_loop(display, controller)

    controller.shutdown_callback = start_game

    def reboot_game(_):        
        controller.running = False

    event_handler = events.FileSystemEventHandler()
    event_handler.on_modified = reboot_game

    observer = observers.Observer()
    observer.schedule(event_handler, path)
    observer.start()
    
    start_game()
    

if __name__ == "__main__":
    main()