#
#   MBC Zwickau Light Client
#
#   Authors: Colin Böttger 
#

from tkinter import *
from  UI.MainWindow.ArduinoInterface import ArduinoInterface

class MainWindow(Frame):
  def __init__(self,parent):
    super().__init__(parent)
    self.Arduino = ArduinoInterface(self, '../Settings/leonardo.json')
    self.Arduino.pack()
