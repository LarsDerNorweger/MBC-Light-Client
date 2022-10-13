#
#   MBC Zwickau Light Client
#
#   Authors: Colin Böttger 
#

from tkinter import *
from tkinter import messagebox

from defines import DEFINES

from  UI.MainWindow.ArduinoInterface import ArduinoInterface
from  UI.MainWindow.GroupManager import Group, GroupsInterface
from UI.MainWindow.SaveInterface import SaveProfileInterface
from  UI.MainWindow.ToolChain import Tools
from UI.MainWindow.GroupSettingsInterface import GroupSettingsInterface

from datamodell import Settings

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
    self.master.resizable(FALSE,FALSE)
    self.master.report_callback_exception = self.__handle_Error
    
 

  def createUI(self):
      setting = Settings(DEFINES.SETTINGS)
      setLanguage(setting.language.speech,'languages\\'+setting.language.path)
      self.Arduino = grid(ArduinoInterface(self, setting.arduino),2,1,rowspan=2)
      self.Arduino.on_click = self.__add_pins_to_group

      self.Tools = grid(Tools(self),1,1,3)
      self.Tools.on_select_all = self.__select_All
      self.Tools.on_delete_from_group = self.__unmark_pins

      self.Groups = grid(GroupsInterface(self, 10),2,2,rowspan=2)
      self.Groups.on_click = self.__change_group

      self.GroupSettings = grid(GroupSettingsInterface(self),2,3)
      self.GroupSettings.group = self.Groups.selected_group

      self.ProfileManager = grid(SaveProfileInterface(self),3,3,sticky=S)
      self.ProfileManager.on_save = lambda:{'groups':self.Groups.groups, 'type':self.Arduino.name}
      self.ProfileManager.on_load = self.__load_Profile

      self.pack()

  def __handle_Error(self, esc, val,tb):
    raise val
    pass
 
  def __load_Profile(self,res):
    if self.Arduino.name != res['type']:
      messagebox.showerror(__("An error occured"),__("The profile requires an Arduino from the type")+' '+res['type'])
      return
    grp = res['groups']
    self.Arduino.toggle_all(True)
    self.__unmark_pins()
    self.Arduino.toggle_all(False)
    self.Groups.reset_groups()
    for i in grp:
      p = i["pins"]
      grp =self.Groups.add_and_create_group(i["name"],i["delay"],p)
      self.Arduino.mark_pins(p,grp.color)
    pass


  def __select_All(self):
    self.Arduino.toggle_all(True)
    self.__add_pins_to_group()
    self.__update_state()
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
    self.__update_state()
    pass

  def __unmark_pins(self):
    group = self.Groups.selected_group
    pins = self.Arduino.selected_pins
    group.Pins = list(set(group.Pins)-set(pins))
    self.Arduino.unmark_pins(pins)
    self.Arduino.toggle_all(False)
    self.__update_state()
    pass

  def __update_state(self):
    self.GroupSettings.group = self.Groups.selected_group
    self.Groups.update()
    pass
