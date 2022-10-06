#
#   MBC Zwickau Light Client
#
#   Authors: Colin Böttger 
#

from tkinter import *
from tkinter import messagebox
from  UI.MainWindow.ArduinoInterface import ArduinoInterface
from  UI.MainWindow.groups import Groups
from  UI.MainWindow.tools import Tools
from UI.translation import setLanguage,__

class MainWindow(Frame):
  def __init__(self,parent):
    super().__init__(parent)
    self.createUI()
    self.master = parent
    


  def createUI(self):
    try:    
      setLanguage('de','./de.json')

      self.Arduino = ArduinoInterface(self, './UI/Settings/leonardo.json')
      self.Arduino.pack()


      self.Tools = Tools(self)
      self.Tools.pack()
      self.Tools.onPinDisable = lambda: self.Arduino.markPins(self.Arduino.getSelectedPins(),"red")
      self.Tools.onClear = lambda:self.Arduino.unselectAll()

      self.Groups = Groups(self, 10)
      self.Groups.pack(side= LEFT)
      self.Arduino.onClick = lambda:self.Arduino.markPins(self.Arduino.getSelectedPins(),self.Groups.getSelectedGroup().color)
      self.pack()
    except Exception as e:
      messagebox.showerror(__("An error occured"),e)
      self.master.destroy()
      

