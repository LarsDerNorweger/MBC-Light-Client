#
#   MBC Zwickau Light Client
#
#   Authors: Colin Böttger 
#


from tkinter import *

from UI.UiHelper import WebsaveColorGenerator,packDown
from UI.translation import __

class Group:
  name:str
  Pins = []
  btn:Radiobutton
  color:str
  delay:int = None

  @property 
  def __dict__(self):
    return {"name":self.name,"pins":self.Pins, "delay":self.delay}


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
    self.groups = []
    self.colors = WebsaveColorGenerator(102)
    self.ed = IntVar()
    self.__generateGroup(GroupCount)


  def __handle_click(self):
    if callable(self.__on_click):
      self.__on_click()
    pass

  def __generateGroup(self,GroupCount):
    for i in range(GroupCount):
      col = next(self.colors)
      grp = Group()
      grp.name = __("group")+" "+str(i)
      grp.btn = packDown(Radiobutton(self,text = grp.name ,bg = col,variable=self.ed ,value=i,command=self.__handle_click))
      grp.color = col
      self.groups.append(grp)
      pass
    pass


  def update(self) -> None:
    for i in self.groups:
      i.btn.config(text=i.name)
      
    return super().update()





