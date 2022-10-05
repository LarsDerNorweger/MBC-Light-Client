#
#   MBC Zwickau Light Client
#
#   Authors: Colin Böttger 
#

from tkinter import *
from  UI.MainWindow.ArduinoInterface import ArduinoInterface
from  UI.MainWindow.tools import Tools

class MainWindow(Frame):
  def __init__(self,parent):
    super().__init__(parent)
    self.createUI()
    

  def createUI(self):
    
    self.Arduino = ArduinoInterface(self, '../Settings/leonardo.json')
    self.Arduino.pack()

    self.Tools = Tools(self)
    self.Tools.pack()

