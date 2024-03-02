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
    parser.add_argument("--port", type=int, default=7777,
      help="The port the OSC server is listening on")
    args = parser.parse_args()

    client = udp_client.SimpleUDPClient(args.ip, args.port)

    #Setting some live parameter values
    for x in range(0, 73, 1):
        client.send_message("/Prompt_Morph", ["X1",1  - float(x/100)])
        time.sleep(1.0)

