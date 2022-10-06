#
#   MBC Zwickau Light Client
#
#   Authors: Colin Böttger 
#

from tkinter import *
from tkinter import messagebox

from  UI.MainWindow.ArduinoInterface import ArduinoInterface
from  UI.MainWindow.groups import GroupsInterface
from  UI.MainWindow.tools import Tools

from UI.translation import setLanguage,__
from UI.UiHelper import grid
class MainWindow(Frame):

  Arduino:ArduinoInterface
  Groups:GroupsInterface

  def __init__(self,parent):
    super().__init__(parent)
    self.createUI()
    self.master = parent
    


  def createUI(self):
    try:    
      setLanguage('de','./de.json')

      self.Arduino = grid(ArduinoInterface(self, './UI/Settings/leonardo.json'),2,1)

      self.Tools = grid(Tools(self),1,1,2)
      
      self.Tools.onPinDisable = lambda: self.Arduino.markPins(self.Arduino.get_selected_pins(),"red")
      self.Tools.onClear = self.__unmark_pins

      self.Groups = grid(GroupsInterface(self, 10),2,2)
      self.Groups.on_click = lambda:self.Arduino.unselect_all() 

      self.Arduino.on_click = self.__add_pins_to_group
      self.pack()
    except Exception as e:
      messagebox.showerror(__("An error occured"),e)
      self.master.destroy()
      

  def __add_pins_to_group(self):
    pins = self.Arduino.get_selected_pins()
    group = self.Groups.get_selected_group()
    group.Pins = group.Pins+list(set(pins)-set(group.Pins))
    print(group.Pins)
    self.Arduino.mark_pins(pins,group.color)
    pass

  def __unmark_pins(self):
    group = self.Groups.get_selected_group()
    pins = self.Arduino.get_selected_pins()
    group.Pins = list(set(group.Pins)-set(pins))
    print(group.Pins)

    self.Arduino.unmark_pins(pins)
    self.Arduino.unselect_all()
    pass

