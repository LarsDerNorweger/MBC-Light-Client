#
#   MBC Zwickau Light Client
#
#   Authors: Colin Böttger 
#

from tkinter import *

from UI.translation import __

class ArduinoDesigner(Frame):
    def __init__(self,master:Tk):
        super().__init__(master)
        master.title(__("create Arduino"))
        pass
    
    