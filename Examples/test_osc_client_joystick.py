"""Small example OSC client that connects to DeforumationQT
    and manipulates PAN values through a controller (Xbox360, etc)
"""
import argparse
import random
import time
from pyjoystick.sdl2 import Key, Joystick, run_event_loop

from pythonosc import udp_client

Axis_left = "-Axis 0"
Axis_right = "Axis 0"
Axis_down = "Axis 1"
Axis_up = "-Axis 1"

if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument("--ip", default="127.0.0.1",
                        help="The ip of the OSC server")
    parser.add_argument("--port", type=int, default=5005,
                        help="The port the OSC server is listening on")
    args = parser.parse_args()

    client = udp_client.SimpleUDPClient(args.ip, args.port)

    def print_add(joy):
        print('Added', joy)


    def print_remove(joy):
        print('Removed', joy)


    def key_received(key):
        #print('received', key)
        if key.value == Key.HAT_UP:
            pass
            # do something
        elif key.value == Key.HAT_DOWN:
            pass
            # do something
        if key.value == Key.HAT_LEFT:
            pass
            # do something
        elif key.value == Key.HAT_UPLEFT:
            pass
            # do something
        elif key.value == Key.HAT_DOWNLEFT:
            pass
            # do something
        elif key.value == Key.HAT_RIGHT:
            pass
            # do something
        elif key.value == Key.HAT_UPRIGHT:
            pass
            # do something
        elif key.value == Key.HAT_DOWNRIGHT:
            pass
            # do something
        elif key.keytype == Key.AXIS:
            if key.keyname == Axis_left:
                if key.value < -0:
                    print(key.keyname + ":" + str(key.value))
                    client.send_message("/Pan_X", key.value)
            elif key.keyname == Axis_right:
                if key.value > 0:
                    print(key.keyname + ":" + str(key.value))
                    client.send_message("/Pan_X", key.value)
            elif key.keyname == Axis_down:
                if key.value > 0:
                    print(key.keyname + ":" + str(key.value))
                    client.send_message("/Pan_Y", key.value)
            elif key.keyname == Axis_up:
                if key.value < -0:
                    print(key.keyname + ":" + str(key.value))
                    client.send_message("/Pan_Y", key.value)
            else:
                print("Other Axis:" + str(key.keyname))

    run_event_loop(print_add, print_remove, key_received)



    live_params = ["/"]
    motion_params = ["Pan_X", "Pan_Y", "Rot_H", "Rot_V", "Zoom", "Tilt"]
    for param in motion_params:
        for x in range(-100,100, 1):
            sendValue = float(x/100)
            client.send_message("/"+param, sendValue)
            print(param + ":" + str(sendValue))
            time.sleep(0.01)
        client.send_message(param, 0)
