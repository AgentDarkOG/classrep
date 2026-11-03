# Phyton Saga

A bright arcade Snake game made with Python and Pygame.

## Run on another Windows device

1. Install Python 3.10 or newer from https://www.python.org/downloads/.
2. Download and extract the `Phyton-Saga-portable.zip` file.
3. Double-click `launch_game.bat`.
4. The launcher installs `pygame-ce` and starts the game.

Internet access is required the first time so Python can install the dependency. After that, the game can run offline.

## Save data

`player_data.json` stores coins, cosmetics, progression, and settings. `high_scores.json` stores the top scores. Keep these files beside `first_class.py`.

## Development run

```text
python -m pip install -r requirements.txt
python first_class.py
```

The `assets` folder must remain beside the game file because it contains the local icons.

## Controls

- `WASD` or arrow keys: steer the snake
- `Touch Swipe`: swipe in the direction you want to move
- `Follow Mouse`: move the cursor toward the direction you want to travel

Choose the control mode from the in-game Settings screen. The selected mode is saved for the next launch.

## Copyright

© 2026 Phyton Saga. All rights reserved.
