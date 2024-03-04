import asyncio
import websockets
import pickle
import time
import ast
import os
import pathlib
needToUpdateMediator = False
anim_args_copy = None
args_copy = None
root_copy = None
connection_string = None
async def sendAsync(value):
    global connection_string
    if connection_string == None:
        deforum_mediator_config_path = os.path.join(pathlib.Path(__file__).parent.absolute(), 'deforum_mediator.cfg')
        if os.path.isfile(deforum_mediator_config_path):
            with open(deforum_mediator_config_path, "r", encoding='utf-8') as def_med_conf:
                connection_string = def_med_conf.readline()
                print("Using connection string:>" + str(connection_string) + "<")
                #connection_string = "ws://localhost:8765"
        else:
            print("Didn't find deforum_mediator.cfg config file. Using connection_string: ws://localhost:8765")
            connection_string = "ws://localhost:8765"

    async with websockets.connect(connection_string) as websocket: #"ws://192.168.1.126:8765") as websocket:
        # await websocket.send(pickle.dumps(value))
        try:
            await asyncio.wait_for(websocket.send(pickle.dumps(value)), timeout=10.0)
            message = await asyncio.wait_for(websocket.recv(), timeout=10.0)
        except TimeoutError:
            print('timeout!')
        #if message.startswith("[\'") and message.endswith("\']"):
        #    message = ast.literal_eval(message)
        #    if len(message) == 1:
        #        message = str(message[0])
        message = pickle.loads(message)
        return message[0]

def mediator_set_anim_args(anim_args, args, root):
    global anim_args_copy
    global args_copy
    global root_copy    
    anim_args_copy = anim_args
    args_copy = args
    root_copy = root

def updateMediator(): #No validation is made that  the websocket server (Mediator.py is actually up and running)
    print("Was ordered to update time_string")
    if anim_args_copy.resume_from_timestring:
        print("Sending Values:" + str(anim_args_copy.resume_timestring))
        return_value = asyncio.run(sendAsync([1, "resume_timestring", anim_args_copy.resume_timestring]))
        #mediator_setValue("resume_timestring", anim_args_copy.resume_timestring)
    else:
        print("Sending Values:" + str(root_copy.timestring))
        return_value = asyncio.run(sendAsync([1, "resume_timestring", root_copy.timestring]))
        #mediator_setValue("resume_timestring", root_copy.timestring) 
    #OUTDIR is the same for either you resume or not.
    mediator_setValue("frame_outdir", args_copy.outdir)


def mediator_getValue(param):
    global needToUpdateMediator
    checkerrorConnecting = True
    needToUpdateMediator = False
    while checkerrorConnecting:
        try:
            return_value = asyncio.run(sendAsync([0, param, 0]))
            if needToUpdateMediator:
                needToUpdateMediator = False
                updateMediator()
            return return_value
        except Exception as e:
            print("Deforum Mediator Error:" + str(e))
            print("...while trying to get parameter ("+str(param)+")")
            print("The Deforumation Mediator, is probably not connected (waiting 2 seconds, before trying to reconnect...)")
            time.sleep(2)
            needToUpdateMediator = True

def mediator_setValue(param, value):
    global needToUpdateMediator
    checkerrorConnecting = True
    needToUpdateMediator = False
    while checkerrorConnecting:
        try:
            return_value = asyncio.run(sendAsync([1, param, value]))
            if needToUpdateMediator:
                needToUpdateMediator = False
                updateMediator()
            return return_value
        except Exception as e:
            print("Deforum Mediator Error:" + str(e))
            print("...while trying to send parameter ("+str(param)+") with value("+str(value)+")")
            print("The Deforumation Mediator, is probably not connected (waiting 2 seconds, before trying to reconnect...)")
            time.sleep(2)
            needToUpdateMediator = True