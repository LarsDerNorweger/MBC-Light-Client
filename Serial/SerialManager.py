#
#   MBC Zwickau Light Client
#
#   Authors: Colin Böttger
#

import threading
import time
import serial
import sys


class SerialManager:
    __stop: bool = False
    lock: threading.Lock

    def __init__(self, port: str, onMessage=None):
        if onMessage is not None:
            self.onMessage = onMessage
        self.__serial = None
        self.__port = port
        self.__thread = threading.Thread(target=self.__CheckForEvents)
        self.lock = threading._allocate_lock()
        pass

    def send(self, msg):
        if self.__serial == None:
            raise Exception("Serialkommunkation not started")
        self.__serial.write(msg)
        print(f"out    => {msg}")

        pass

    def sendLine(self, msg):
        self.__serial.write(bytes(msg, "utf8"))
        self.__serial.write(bytes("\n", "utf8"))
        print(f"out    => {msg}")

    def start(self):
        self.__serial = serial.Serial(self.__port, baudrate=115200)
        self.__thread.start()

    def stop(self):
        self.lock.acquire()
        self.__stop = True
        self.lock.release()

    @property
    def onMessage(self):
        return None

    @onMessage.setter
    def onMessage(self, value):
        if not callable(value):
            raise Exception("Messagehandler must be callable")
        self.__handleMessage = value

    def __CheckForEvents(self):
        while True:
            self.lock.acquire()
            if (self.__stop):
                break
            self.lock.release()

            data = self.__serial.read_all()
            if (data != bytes('', "utf8")):
                print(f"income <= {data}")
                self.__handleMessage(self, data)

        self.lock.release()
        print("Thread stoped")
        pass

    __start = False
    __port: str
    __serial: serial.Serial
