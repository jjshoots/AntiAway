import pyautogui
from pynput import keyboard
from pynput import mouse
import random
import time

class AntiAway_Class:
    def __init__(self):
        self.size_x, self.size_y = pyautogui.size()
        self.size_x *= 0.5
        self.size_y *= 0.5
        self.time_since_idle = time.time()

        self.start_listeners()

    # moves mouse
    def move_linear(self):
        pyautogui.moveTo(self.size_x+10, self.size_y+10, 0.2)
        pyautogui.moveTo(self.size_x-10, self.size_y-10, 0.2)

    # presses numlock twice in quick succession
    def press_numlock(self):
        pyautogui.press('numlock', presses=2, interval=0.4)

    # key on press function
    def on_press(self, key):
        self.time_since_idle = time.time()

    # mouse on move function
    def on_move(self, x, y):
        self.time_since_idle = time.time()

    # keyboard and mouse listeners
    def start_listeners(self):
        self.keeb_listener = keyboard.Listener(on_press=self.on_press)
        self.keeb_listener.start()

        self.mouse_listener = mouse.Listener(on_move=self.on_move)
        self.mouse_listener.start()

    # delta in seconds since idle
    def get_delta_since_idle(self):
        return time.time() - self.time_since_idle
        

