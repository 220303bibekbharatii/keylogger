from pynput.mouse import Controller as MouseController
from pynput.keyboard import Controller as KeyboardController

def controlMouse():
    mouse = MouseController()
    mouse.position = (10, 20)

def controlKeyboard():
    keyboard = KeyboardController()
    keyboard.type("hello!")

controlKeyboard()
