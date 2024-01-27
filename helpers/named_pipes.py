import win32pipe, win32file, pywintypes
import pickle
import asyncio
import time
class Deforumation_Named_Pipes():
    def __init__(self, deforumation_settings=None, parent=None):
        if deforumation_settings != None:
            self.deforumation_settings = deforumation_settings
        else:
            pass
        self.parent = parent

    async def sendAsync(self, value, special=False):
        bufSize = 64 * 1024
        handle = win32file.CreateFile('\\\\.\\pipe\\Deforumation', win32file.GENERIC_READ | win32file.GENERIC_WRITE, 0, None, win32file.OPEN_EXISTING, 0, None)
        res = win32pipe.SetNamedPipeHandleState(handle, win32pipe.PIPE_READMODE_MESSAGE, None, None)
        bytesToSend = pickle.dumps(value)
        win32file.WriteFile(handle, bytesToSend)
        result, data = win32file.ReadFile(handle, bufSize)
        message = data
        while len(data) == bufSize:
            print("More data has to be read (normal pipe async):" + str(len(data)))
            result, data = win32file.ReadFile(handle, bufSize)
            message += data

        win32file.CloseHandle(handle)
        #If special is True, many values will have been returned, and so the message is a chunk of parameters and values
        if special== True:
            return message
        #Only one parameter has been returned, so decode it and return the value of it.
        message = pickle.loads(message)
        if isinstance(message, list):
            if len(message) == 1:
                return message[0]
            else:
                return message
        return message[0]

    def closeEvent(self, event):
        print("Deforumation is closing")
    def writeValue(self, param, value, special=False):
        #Start by adding the new value to our config
        self.deforumation_settings.writeDeforumSendValuesToConfig(param, value)
        checkerrorConnecting = True
        while checkerrorConnecting:
            try:
                asyncio.run(self.sendAsync([1, param, value], special))
                checkerrorConnecting = False
            except Exception as e:
                print("Deforumation Mediator Write Error:" + str(e))
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

    def waitForNewImageFromDeforum(self):
        #global current_live_view_pipe
        current_live_view_pipe = None
        bufSize = 64 * 1024
        value = -1
        try:
            current_live_view_pipe = win32pipe.CreateNamedPipe('\\\\.\\pipe\\deforumation_pipe_in', win32pipe.PIPE_ACCESS_DUPLEX, win32pipe.PIPE_TYPE_MESSAGE | win32pipe.PIPE_READMODE_MESSAGE | win32pipe.PIPE_WAIT, 1, 65536, 65536, 0, None)

            win32pipe.ConnectNamedPipe(current_live_view_pipe, None)
            message = win32pipe.SetNamedPipeHandleState(current_live_view_pipe, win32pipe.PIPE_READMODE_MESSAGE, None, None)
            if message == 0:
                print(f"SetNamedPipeHandleState return code: {message}")
                value = 0
                return value
            else:
                totalToSend = []
                result, data = win32file.ReadFile(current_live_view_pipe, bufSize)
                message = data
                while len(data) == bufSize:
                    print("More data has to be read (special pipe async):" + str(len(data)))
                    result, data = win32file.ReadFile(current_live_view_pipe, bufSize)
                    message += data

                arr = pickle.loads(message)
            if len(arr) == 3:
                shouldWrite = arr[0]
                parameter = arr[1]
                value = arr[2]
                if str(parameter) == "new_image_created":
                    #print(f"New image received, image number:{value}")
                    value = value
                elif str(parameter) == "close_thread":
                    value = -666
            #Wether right or wrong, returns have to be made, and handles need to be closed ;)
            win32file.WriteFile(current_live_view_pipe, b"OK")
            win32file.CloseHandle(current_live_view_pipe)
            #print("Receive loop done!")
        except Exception as e:
            print("Error:" + str(e))
            if current_live_view_pipe != None:
                win32file.CloseHandle(current_live_view_pipe)
            else:
                print("DeforumationQT already running. Exiting.")
                self.parent.shouldExitLiveView = True
                value = -666
        return value

    def CloseCommunicationThread(self):
        try:
            bufSize = 64 * 1024
            handle = win32file.CreateFile('\\\\.\\pipe\\deforumation_pipe_in', win32file.GENERIC_READ | win32file.GENERIC_WRITE, 0, None, win32file.OPEN_EXISTING, 0, None)
            value = [1, "close_thread", 0]
            bytesToSend = pickle.dumps(value)
            win32file.WriteFile(handle, bytesToSend)
            # Need to receive back data to close the write call (but totally discards this)
            #print("AWaiting reply")
            result, data = win32file.ReadFile(handle, bufSize)
            message = data
            while len(data) == bufSize:
                print("More data has to be read (normal pipe async):" + str(len(data)))
                result, data = win32file.ReadFile(handle, bufSize)
                message += data
            #print("Got reply:" + str(message))
        except pywintypes.error as e:
            print("Something went wrong when trying to end the named pipe live view thread")

    def sendAllMotionValues(self):
        SendBlock = []
        self.writeValue("<BLOCK>", SendBlock)