# Chrome T-Rex Bot

A Python bot that plays Chrome's offline T-Rex game by reading screen pixels and pressing the space bar at the right moment. No game internals or browser automation are used, only what is visible on screen.

Game: https://elgoog.im/t-rex/

## How it works

- A small "sensor box" sits just in front of the T-Rex.
- Every ~10 ms, the bot grabs that region with Pillow and compares its darkest and lightest pixels to the background colour.
- If anything differs enough (a cactus, for example), `pyautogui` presses space and the dino jumps.
- The box widens over time to look further ahead, because the game speeds up.
- Comparing against the live background colour means it also works in night mode.

## Requirements

- Windows
- Python 3.10+
- Chrome at 100% zoom

```
pip install pillow pyautogui
```

## Setup

1. Open the game in Chrome with the dino visible, not started.
2. Find your screen coordinates with `pyautogui.position()` and set these in `main.py`:
   - `X1, Y1`: the right edge of the T-Rex's face, level with a cactus's middle
   - `GAME_CLICK`: any empty spot inside the game area
3. Run `main.py`, then switch to Chrome.

To stop: press Stop in your IDE, or move the mouse to the top-left corner of the screen (pyautogui failsafe).

## Settings

| Name | Purpose |
|---|---|
| `HEIGHT` | Height of the sensor box |
| `BASE_WIDTH` | Starting look-ahead distance (px) |
| `SPEEDUP` | Extra look-ahead gained per second (px) |
| `THRESHOLD` | How different from the background counts as an obstacle |

## Known limitations

- Birds at head height also trigger a jump (ducking is not implemented yet).
- Coordinates are specific to one screen layout, so recalibrate if you move or resize the window.

## Ideas for next steps

- Duck under birds with a second, higher sensor box
- Auto-calibrate by locating the dino on screen