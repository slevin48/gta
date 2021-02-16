# directkeys2.py

from pynput.keyboard import Key, Controller

keyboard = Controller()

Z = "z"
Q = "q"
D = "d"
S = "s"

def PressKey(key):
    keyboard.press(key)

def ReleaseKey(key):
    keyboard.release(key)

