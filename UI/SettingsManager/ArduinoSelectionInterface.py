#
#   MBC Zwickau Light Client
#
#   Authors: Colin Böttger 
#

from defines import DEFINES

from tkinter import *
from tkinter import ttk
from UI.UiHelper import packSide
from UI.translation import __

import json

from datamodell import Arduino, Settings

class ArduinoSelectionInterface(Frame):

  @property
  def selected_arduino(self):
    ard = self.__selected_Arduino.get()
    return Arduino(ard, self.Arduinos[ard])

  def __init__(self,master,settings:Settings):
    super().__init__(master)
    if(settings.arduino):
      ard  = settings.arduino.typ
      self.__selected_Arduino = StringVar(self,ard)
    else: self.__selected_Arduino = StringVar(self)

    self.Arduinos = ArduinoSelectionInterface.__get_arduinos(DEFINES.ARDUINO_PATH)
    self.createUI()
    pass

  def createUI(self):
    packSide(Label(self,text=__("Arduino :")))
    cb = packSide(ttk.Combobox(self,textvariable=self.__selected_Arduino))
    keys = []
    for i in self.Arduinos.keys():
      keys.append(i)
    cb["values"]=keys
    pass

  @staticmethod
  def __get_arduinos(path:str):
    with open(path) as fs:
      res = ''.join(fs.readlines())
      return json.loads(res)