#
#   MBC Zwickau Light Client
#
#   Authors: Colin Böttger 
#

from ctypes import alignment
from tkinter import *
from  UI.translation import __

class Tools(Frame):
  def __init__(self,parent):
    super().__init__(parent)
    self.createUI()    

  def createUI(self):
    Button(self,text = __("enable pin")).pack(side=LEFT)
    Button(self).pack(side=LEFT)
    Button(self).pack(side=LEFT)
    Button(self).pack(side=LEFT)
    Button(self).pack(side=LEFT)

