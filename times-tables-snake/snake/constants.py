import pygame


BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
RED = (255, 0, 0)
GREEN = (0, 255, 0)
BLUE = (0, 0, 255)

SCREEN_DIMENSIONS = (800, 600)
SNAKE_SEGMENT_DIMENSIONS = (15, 15)

TEXT_FONT = 'freesansbold.ttf'
TEXT_SIZE = 12

SPEED = 5

TIMES_TABLE_BASE = 2
TIMES_TABLE_RANGE = (0, 15)

NUMBER_OF_OPTIONS = 10

TITLE_START = f"{TIMES_TABLE_BASE} Times Tables   |    Maths Snake    |   "

MOMENTUM_MAP = {
    pygame.K_DOWN: (0, SPEED),
    pygame.K_UP: (0, -SPEED),
    pygame.K_LEFT: (-SPEED, 0),
    pygame.K_RIGHT: (SPEED, 0)
}
