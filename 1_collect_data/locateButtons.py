# locateButtons.py
import pyautogui
def click_play_button_off():
 """
 Double-click the "play_button_off.PNG" match. 
 Move the mouse cursor off the button to prevent obscuring the button in later checks.
 """
 pyautogui.doubleClick(r'screenshots/play_button_off.PNG')
 pyautogui.moveTo(1000, 1000, duration=0)
def click_stop_button_off():
 """
 Double-click the "stop_button_off.PNG" match. 
 Move the mouse cursor off the button to prevent obscuring the button in later checks.
 """
 pyautogui.doubleClick(r'screenshots/stop_button_off.PNG')
 pyautogui.moveTo(1000, 1000, duration=0)
def detect_play_button_on():
 """
 Check if the "play_button_on.PNG" can be found, meaning that the macro is running.
 """
 if pyautogui.locateOnScreen(r'screenshots/play_button_on.PNG'):
  return True
 else:
  return False
def detect_stop_button_on():
 """
 Check if the "stop_button_on.PNG" can be found, meaning that the macro is not running.
 """
 if pyautogui.locateOnScreen(r'screenshots/stop_button_on.PNG'):
  return True
 else:
  return False