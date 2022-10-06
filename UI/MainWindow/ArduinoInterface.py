#
#   MBC Zwickau Light Client
#
#   Authors: Colin Böttger 
#

from tkinter import *
from tkinter import messagebox
from typing import List
from UI.translation import __
import json

class ArduinoInterface(Frame):

  @property    
  def onClick(self)->None:
      return None
  @onClick.setter
  def onClick(self,value):
      self.__onClick = value

  def __init__(self,parent:Frame,path:str):
    super().__init__(parent)
    self.Pins:List[PIN] = []
    self.loadArduino(path)
    self.createArduino()
    self.__onClick = None
    pass

  def __handleClick(self):
    if callable(self.__onClick):
      self.__onClick()
    pass

  def createArduino(self):
    for i,pin in enumerate(self.Pins):
      c = int(i%2)
      cb = Checkbutton(self,text = f'PIN {pin.pinNumber}',variable=pin.var, command=lambda:self.__handleClick())
      cb.grid(column=c,row= int((i-c)/2),sticky=W)
      pin.cb = cb
      pass
    pass

  def loadArduino(self,path:str):
    try:
      with open(path) as fs:
          res = json.loads(" ".join(fs.readlines()))["pins"]
          for i in res:
            p = PIN(i)
            p.var = BooleanVar()
            self.Pins.append(p)
      pass
    except EOFError:
      messagebox.showerror("Load Failed","Unable to Load Arduino Profile")
      pass
    pass

  def getSelectedPins(self):
    res = []
    for pin in self.Pins:
      if pin.var.get() == True:
        res.append(pin.pinNumber)
    return res

  def unselectAll(self):
    for pin in self.Pins:
      pin.var.set(False)
    pass

  def markPins(self,pins,color:str):
    for pin in self.Pins:
      if pin.pinNumber in pins:
        pin.cb.config(bg = color)
    pass
  
class PIN:
  pinNumber:int
  var:BooleanVar
  cb:Checkbutton
  def __init__(self,number):
    self.pinNumber = number
    pass