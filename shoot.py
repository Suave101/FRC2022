from __future__ import print_function
import playsound
from inputs import get_gamepads
shooting = False


def main():
    global shooting
    while True:
        events = get_gamepad()
        for event in events:
            if event.cod "BTN_TR" and event.state == 1:
                if not shooting:
                    playsound.playsound(bs)

