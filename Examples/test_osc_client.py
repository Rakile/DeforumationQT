"""Small example OSC client that connects to DeforumationQT
    and manipulates values
"""
import argparse
import random
import time

from pythonosc import udp_client


if __name__ == "__main__":

    parser = argparse.ArgumentParser()
    parser.add_argument("--ip", default="127.0.0.1",
      help="The ip of the OSC server")
    parser.add_argument("--port", type=int, default=5005,
      help="The port the OSC server is listening on")
    args = parser.parse_args()

    client = udp_client.SimpleUDPClient(args.ip, args.port)

    #Setting some live parameter values
    client.send_message("/Sampler_Steps", 40)
    client.send_message("/CFG_Scale", 2)
    client.send_message("/Strength", 0.65)
    client.send_message("/Cadence", 3)
    client.send_message("/Noise_Multiplier", 1.08)

    #Setting some motion parameter values
    motion_params = ["Pan_X", "Pan_Y", "Rot_H", "Rot_V", "Zoom", "Tilt"]
    for param in motion_params:
        for x in range(-100,100, 1):
            sendValue = float(x/100)
            client.send_message("/"+param, sendValue)
            print(param + ":" + str(sendValue))
            time.sleep(0.01)
        client.send_message(param, 0)
