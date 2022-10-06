#

#   MBC Zwickau Light Client

#

#   Authors: Colin Böttger 

#


from tkinter import *

from UI.UiHelper import WebsaveColorGenerator

class Group:
  Pins = []

  btn:Radiobutton
  color:str

class Groups(Frame):

  def __init__(self,master,GroupCount):

    super().__init__(master)

    self.groups = []

    self.colors = WebsaveColorGenerator(102)
    self.ed = IntVar()
    self.__generateGroup(GroupCount)


  def __generateGroup(self,GroupCount):

    for i in range(GroupCount):

      col = next(self.colors)

      rb = Radiobutton(self,text = f"Group {i}",bg = col,variable=self.ed ,value=i)

      rb.pack()

      grp = Group()
      grp.btn = rb
      grp.color = col
      self.groups.append(grp)
      pass
    pass

  def getSelectedGroup(self)->Group:
    return self.groups[self.ed.get()]




