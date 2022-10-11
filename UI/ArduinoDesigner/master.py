#
#   MBC Zwickau Light Client
#
#   Authors: Colin Böttger 
#

from tkinter import *
from UI.SettingsManager.datamodell import Reload

from UI.translation import __
from UI.UiHelper import grid
from UI.ArduinoDesigner.Input import ArduinoInput

class ArduinoDesigner(Frame):
    def __init__(self,master:Tk):
        super().__init__(master)
        self.on_close = None
        master.protocol("WM_DELETE_WINDOW", self.__handle_close)
        self.master = master
        self.master.title(__("create Arduino"))
        self.createUI()
        self.pack()
        pass

    def createUI(self):
        grid(Label(self,text = __("create Arduino")),0,0,columnspan=2)
        self.input = grid(ArduinoInput(self),1,0,columnspan=2)
        grid(Button(self,text=__("Save"),command=self.__handle_save),2,0)
        grid(Button(self,text=__("Cancle"),command=self.__handle_close),2,1)

    def __handle_save(self):
        self.master.destroy()
        raise Reload

    def __handle_close(self):
        if callable(self.on_close):
            self.on_close()



    
    