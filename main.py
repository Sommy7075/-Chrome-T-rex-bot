import ctypes
import time
import pyautogui
from PIL import ImageGrab

ctypes.windll.user32.SetProcessDPIAware()  # must run before any screen grabbing

X1, Y1 = 1821, 1286      # from your calibration
HEIGHT = 25
BASE_WIDTH = 70
SPEEDUP = 1.5
THRESHOLD = 40
GAME_CLICK = (844, 677)


def background_brightness():
    img = ImageGrab.grab(bbox=(X1, Y1 - 40, X1 + 1, Y1 - 39)).convert("L")
    return img.getpixel((0, 0))


def obstacle_ahead(width):
    img = ImageGrab.grab(bbox=(X1, Y1, X1 + width, Y1 + HEIGHT)).convert("L")
    lo, hi = img.getextrema()
    bg = background_brightness()
    return abs(lo - bg) > THRESHOLD or abs(hi - bg) > THRESHOLD


pyautogui.click(GAME_CLICK)
pyautogui.press("space")
start = time.time()

while True:
    width = BASE_WIDTH + (time.time() - start) * SPEEDUP
    if obstacle_ahead(int(width)):
        pyautogui.press("space")
    time.sleep(0.01)