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
  def on_click(self)->None:
      return None
  @on_click.setter
  def on_click(self,value):
      self.__onClick = value

  def __init__(self,parent:Frame,path:str):
    super().__init__(parent)
    self.Pins:List[PIN] = []
    self.__load_arduino(path)
    self.__create_arduino()
    self.__onClick = None
    pass

  def __handle_click(self):
    if callable(self.__onClick):
      self.__onClick()
    pass

  def __create_arduino(self):
    for i,pin in enumerate(self.Pins):
      c = int(i%2)
      cb = Checkbutton(self,text = f'PIN {pin.pinNumber}',variable=pin.var, command=lambda:self.__handle_click())
      cb.grid(column=c,row= int((i-c)/2),sticky=W)
      pin.cb = cb
      pass
    pass

  def __load_arduino(self,path:str):
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

  def get_selected_pins(self):
    res = []
    for pin in self.Pins:
      if pin.var.get() == True:
        res.append(pin.pinNumber)
    return res

  def unselect_all(self):
    for pin in self.Pins:
      pin.var.set(False)
    pass

  def mark_pins(self,pins,color:str):
    for pin in self.Pins:
      if pin.pinNumber in pins:
        pin.cb.config(bg = color)
    pass

  def unmark_pins(self,pins):
    for pin in self.Pins:
      if pin.pinNumber in pins:
        pin.cb.config(bg = "white")
    pass
  
class PIN:
  pinNumber:int
  var:BooleanVar
  cb:Checkbutton
  def __init__(self,number):
    self.pinNumber = number
    pass