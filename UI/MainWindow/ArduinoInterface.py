#
#   MBC Zwickau Light Client
#
#   Authors: Colin Böttger 
#

from tkinter import *
from tkinter import messagebox
from typing import List
from UI.MainWindow.GroupManager import Group
from UI.translation import __
from UI.UiHelper import grid
import json

from UI.SettingsManager.datamodell import Arduino

class ArduinoInterface(Frame):

  @property    
  def on_click(self)->None:
      return None
  @on_click.setter
  def on_click(self,value):
      self.__onClick = value

  @property
  def name(self):
    return self.__name

  @property
  def selected_pins(self):
    res = []
    for pin in self.Pins:
      if pin.var.get() == True:
        res.append(pin.pinNumber)
    return res

  def __init__(self,parent:Frame,arduino:Arduino):
    super().__init__(parent)
    self.Pins:List[PIN] = []
    if arduino is None:
      Label(self, text=__("No arduino loaded")).pack()
      return
    self.__load_arduino(arduino)
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
      pin.cb = grid(cb,int((i-c)/2),c,sticky=W)
      pass
    pass

  def __load_arduino(self,arduino:Arduino):
    try:
      for i in arduino.pins:
        p = PIN(i)
        p.var = BooleanVar()
        self.Pins.append(p)
      self.__name = arduino.typ
      pass
    except EOFError:
      messagebox.showerror("Load Failed","Unable to Load Arduino Profile")
      pass
    pass

  def toggle_all(self,force= None):
    for pin in self.Pins:
      pin.var.set(force if force != None else not pin.var.get())
    pass

  def mark_pins(self,pins,color:str):
    for pin in self.Pins:
      if pin.pinNumber in pins:
        pin.cb.config(bg = color)
    pass

  def unmark_pins(self,pins):
    for pin in self.Pins:
      if pin.pinNumber in pins:
        pin.cb.config(bg = self.cget('bg'))
    pass

  __name:str

  
class PIN:
  pinNumber:int
  var:BooleanVar
  cb:Checkbutton
  def __init__(self,number):
    self.pinNumber = number
    pass