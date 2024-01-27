import asyncio
import websockets
import pickle
import time

class Deforumation_Websockets():
    def __init__(self, mediator_address, mediator_port, deforumation_address, deforumation_port, deforumation_self_address, deforumation_settings=None, parent=None):
        if deforumation_settings != None:
            self.deforumation_settings = deforumation_settings
        else:
            pass
        self.stop = None
        self.server = None
        self.serverShutDown = False
        self.value = None
        self.mediator_address = mediator_address
        self.mediator_port = mediator_port
        self.deforumation_address = deforumation_address
        self.deforumation_port = deforumation_port
        self.deforumation_self_address = deforumation_self_address

    async def sendAsync(self, value, special=False):
        async with websockets.connect("ws://"+ self.mediator_address + ":" + self.mediator_port) as websocket:
            # await websocket.send(pickle.dumps(value))
            try:
                await asyncio.wait_for(websocket.send(pickle.dumps(value)), timeout=10.0)
                message = await asyncio.wait_for(websocket.recv(), timeout=10.0)
                if special == True:
                    return message
                message = pickle.loads(message)
                if isinstance(message, list):
                    if len(message) == 1:
                        return message[0]
                    else:
                        return message
                return message[0]

            except TimeoutError:
                print('timeout!')
            return None


    def closeEvent(self, event):
        print("Deforumation is closing")

    def writeValue(self, param, value):
        # Start by adding the new value to our config
        self.deforumation_settings.writeDeforumSendValuesToConfig(param, value)
        checkerrorConnecting = True
        while checkerrorConnecting:
            try:
                asyncio.run(self.sendAsync([1, param, value]))
                checkerrorConnecting = False
            except Exception as e:
                # print("Deforumation Mediator Error:" + str(e))
                # print("The Deforumation Mediator, is probably not connected (waiting 5 seconds, before trying to reconnect...)")
                time.sleep(0.05)

    def readValue(self, param, value=-1, special=False):
        checkerrorConnecting = True
        while checkerrorConnecting:
            try:
                return_value = asyncio.run(self.sendAsync([0, param, value], special))
                if return_value != None:
                    if not special:
                        self.deforumation_settings.writeDeforumReceiveValuesToConfig(param, return_value)
                    return return_value
            except Exception as e:
                # print("Exception number:" + str(e.args[0]))
                if e.args[0] != 231 and e.args[0] != 2:
                    print("Deforumation Mediator Read Error:" + str(e))
                time.sleep(0.05)

    async def main_websocket(self, websocket, path, queue):
        # print("websocket:" + str(websocket))
        message = await websocket.recv() #async for message in websocket:
        # print("Incomming message:"+str(message))
        arr = pickle.loads(message)
        if len(arr) == 3:
            shouldWrite = arr[0]
            parameter = arr[1]
            self.value = arr[2]
            if str(parameter) == "new_image_created":
                #print(f"New image received, image number:{self.value}")
                self.value = self.value
            elif str(parameter) == "close_thread":
                self.value = -666
        await websocket.send(b"OK")
        await queue.put(self.value)


    async def async_waitForNewImageFromDeforum(self, port):
        global stop
        global server
        self.value = None
        queue = asyncio.Queue()
        try:
            stop = asyncio.Future()  # run forever
            async with websockets.serve(lambda ws, path: self.main_websocket(ws, path, queue), self.deforumation_address, int(self.deforumation_port)):
                message = await queue.get()
        except KeyboardInterrupt:
            server.close()
            print("Ctrl-c :)")
        return message

    def waitForNewImageFromDeforum(self, port=8767):
        loop = asyncio.new_event_loop()
        asyncio.set_event_loop(loop)

        message = loop.run_until_complete(self.async_waitForNewImageFromDeforum(port))
        loop.close()
        return message

    async def async_CloseCommunicationThread(self, port):
        message = None
        try:
            #connect_string = "ws://" + self.deforumation_self_address + ":" + str(self.deforumation_port)
            async with websockets.connect("ws://" + self.deforumation_self_address + ":" + str(self.deforumation_port)) as websocket:
                try:
                    value = [1, "close_thread", 0]
                    bytesToSend = pickle.dumps(value)
                    await asyncio.wait_for(websocket.send(bytesToSend), timeout=10.0)
                    message = await asyncio.wait_for(websocket.recv(), timeout=10.0)  # We don't care about the message
                    print("Got reply:" + str(message))
                except TimeoutError:
                    print('timeout!')
        except Exception as e:
            print("Couldn't close websocket thread")

    def CloseCommunicationThread(self):
        loop = asyncio.new_event_loop()
        asyncio.set_event_loop(loop)
        loop.run_until_complete(self.async_CloseCommunicationThread(port=8767))
        loop.close()

