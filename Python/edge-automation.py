import subprocess
import time
import pyautogui

EDGE_PATH = r"C:\Program Files (x86)\Microsoft\Edge\Application\msedge.exe"
SEARCH_ENGINE = "Yahoo"

edge_process = subprocess.Popen([EDGE_PATH])

time.sleep(5)

pyautogui.hotkey("ctrl", "l")
pyautogui.write("edge://settings/searchEngines")
pyautogui.press("enter")

time.sleep(5)

for _ in range(4):
    pyautogui.press("tab")
    time.sleep(0.2)

pyautogui.write(SEARCH_ENGINE)

time.sleep(2)

three_dots = pyautogui.locateCenterOnScreen(
    "three_dots.jpg",
    confidence=0.8
)

if not three_dots:
    raise Exception("Three-dot menu not found")

print(f"Three-dot menu found at: {three_dots}")

pyautogui.click(three_dots)

time.sleep(1)
OFFSET_X = 15

set_default_coord = (three_dots[0] + OFFSET_X, three_dots[1])

if not set_default_coord:
    raise Exception("Set Default option not found")

print(f"Set Default found at: {set_default_coord}")

pyautogui.click(set_default_coord)

print(f"{SEARCH_ENGINE} set as default search engine.")

time.sleep(5)

close_button = pyautogui.locateCenterOnScreen(
    "close.jpg",
    confidence=0.8
)

if not close_button:
    raise Exception("Close button not found")

print(f"Close button found at: {close_button}")

pyautogui.click(close_button)
