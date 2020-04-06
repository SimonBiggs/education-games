#!/bin/bash

export PATH="$HOME/.pyenv/bin:$PATH"
eval "$(pyenv init -)"
eval "$(pyenv virtualenv-init -)"

gnome-terminal -e 'sh -c "python ./livereload.py; read -p \"Press [Enter] key to quit...\""'