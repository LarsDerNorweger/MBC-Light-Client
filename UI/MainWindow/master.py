#
#   MBC Zwickau Light Client
#
#   Authors: Colin Böttger 
#

from tkinter import *
from tkinter import messagebox

from  UI.MainWindow.ArduinoInterface import ArduinoInterface
from  UI.MainWindow.GroupManager import GroupsInterface
from UI.MainWindow.SaveInterface import SaveProfileInterface
from  UI.MainWindow.ToolChain import Tools
from UI.MainWindow.GroupSettingsInterface import GroupSettingsInterface

from UI.translation import setLanguage,__
from UI.UiHelper import grid
class MainWindow(Frame):

  Arduino:ArduinoInterface
  Groups:GroupsInterface
  GroupSettings:GroupSettingsInterface
  ProfileManager:SaveProfileInterface

  def __init__(self,parent):
    super().__init__(parent)
    self.createUI()
    self.master = parent
    self.master.title("MBC Lux")
    
 

  def createUI(self):
      setLanguage('de','./de.json')

      self.Arduino = grid(ArduinoInterface(self, './UI/Settings/leonardo.json'),2,1,rowspan=2)
      self.Arduino.on_click = self.__add_pins_to_group

      self.Tools = grid(Tools(self),1,1,3)
      self.Tools.on_select_all = self.__select_All
      self.Tools.on_delete_from_group = self.__unmark_pins

      self.Groups = grid(GroupsInterface(self, 10),2,2,rowspan=2)
      self.Groups.on_click = self.__change_group

      self.GroupSettings = grid(GroupSettingsInterface(self),2,3)
      self.GroupSettings.group = self.Groups.selected_group

      self.ProfileManager = grid(SaveProfileInterface(self),3,3,sticky=S)
      self.ProfileManager.on_save = lambda:self.Groups.groups

      self.pack()
 
      
  def __select_All(self):
    self.Arduino.toggle_all(True)
    self.__add_pins_to_group()
    pass

  def __change_group(self):
    self.Arduino.toggle_all(False)
    self.GroupSettings.group = self.Groups.selected_group
    self.Groups.update()
    pass

  def __add_pins_to_group(self):
    pins = self.Arduino.selected_pins
    group = self.Groups.selected_group
    group.Pins = group.Pins+list(set(pins)-set(group.Pins))
    self.Arduino.mark_pins(pins,group.color)
    pass

  def __unmark_pins(self):
    group = self.Groups.selected_group
    pins = self.Arduino.selected_pins
    group.Pins = list(set(group.Pins)-set(pins))
    self.Arduino.unmark_pins(pins)
    self.Arduino.toggle_all(False)
    pass


