#
#   MBC Zwickau Light Client
#
#   Authors: Colin Böttger 
#

from tkinter import *

class ArduinoInterface(Frame):
  def __init__(self,parent:Frame,path:str):
    super().__init__(parent)
    self.loadArduino(path)

  def loadArduino(self,path:str):
    pass

  
    