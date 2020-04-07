#!/bin/bash

export PATH="$HOME/.pyenv/bin:$PATH"
eval "$(pyenv init -)"
eval "$(pyenv virtualenv-init -)"

gnome-terminal -e 'sh -c "python -m snake.__main__; read -p \"Press [Enter] key to quit...\""'