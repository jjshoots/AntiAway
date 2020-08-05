from AntiAway_Class import AntiAway_Class
import time

AntiAway = AntiAway_Class()

while __name__ == '__main__':
    delta = AntiAway.get_delta_since_idle()

    if(delta > 240):
        # AntiAway.move_linear()
        AntiAway.press_numlock()

    time.sleep(60)