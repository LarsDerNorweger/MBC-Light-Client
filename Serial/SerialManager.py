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
  __stop:bool = False
  
  def __init__(self, port:str,onMessage=None):
    self.onMessage = onMessage
    self.__port = port
    self.__thread = threading.Thread(target =self.__CheckForEvents)
    pass

  def sendLine(self,msg):
    if self.__serial == None:
      raise Exception("Serialkommunkation not started")

    print(f"out    => {msg}")
    self.__serial.write(bytes(msg,'utf8'))
    self.__serial.write(bytes('\n','utf8'))

  def start(self):
    self.__serial = serial.Serial(self.__port,baudrate=115200)
    self.__thread.start()

  def stop(self):
    self.__stop = True

  @property
  def onMessage(self):
    return None
  
  @onMessage.setter
  def onMessage(self,value):
    if not callable(value):
      raise Exception("Messagehandler must be callable")
    self.__handleMessage = value

  def __CheckForEvents(self):
    while not self.__stop:
      data = self.__serial.readline()
      if(data != ''):
          print(f"income <= {data}")
          self.__handleMessage(self,data)
      

    print("Thread stoped")
    pass

  __start = False
  __port:str 
  __serial:serial.Serial
