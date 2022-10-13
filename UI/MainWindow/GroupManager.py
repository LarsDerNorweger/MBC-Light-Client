#
#   MBC Zwickau Light Client
#
#   Authors: Colin Böttger 
#


from tkinter import *

from datamodell import Group
from UI.UiHelper import WebsaveColorGenerator,packDown
from UI.translation import __



class GroupsInterface(Frame):
  @property    
  def on_click(self)->None:
      return None
  @on_click.setter
  def on_click(self,value):
      self.__on_click = value

  @property
  def selected_group(self)-> Group:
    return self.groups[self.ed.get()]

  def __init__(self,master,GroupCount):
    super().__init__(master)
    self.__on_click = None
    self.groups:List[Group] = []
    self.reset_groups()
    self.ed = IntVar()
    self.__generateGroup(GroupCount)

  def __handle_click(self):
    if callable(self.__on_click):
      self.__on_click()
    pass

  def __generateGroup(self,GroupCount):
    for i in range(GroupCount):
      self.add_and_create_group(str(__("group")+' '+str(i)),0)
      pass
    pass

  def reset_groups(self):
    for grp in self.groups:      
      grp.btn.destroy()

    self.groups = []
    self.colors = WebsaveColorGenerator(102)
    pass

  def add_and_create_group(self,name:str,delay:int,pins = [])->Group:
    grp = Group()
    grp.name = name
    grp.delay = delay if delay==None else 0
    grp.color = next(self.colors)
    grp.Pins = pins
    grp.btn = packDown(Radiobutton(self,text = grp.name ,bg = grp.color,variable=self.ed ,value=len(self.groups),command=self.__handle_click))
    self.groups.append(grp)
    return grp

  def update(self) -> None:
    for i in self.groups:
      i.btn.config(text=i.name)
    return super().update()