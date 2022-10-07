#
#   MBC Zwickau Light Client
#
#   Authors: Colin Böttger 
#

from ctypes import alignment
from signal import raise_signal
from tkinter import *
from  UI.translation import __
from UI.UiHelper import packSide
from UI.ArduinoDesigner.master import ArduinoDesigner

class Tools(Frame):

    @property    
    def onPinEnable(self)->None:
        return None
    @onPinEnable.setter
    def onPinEnable(self,value):
        self.__onEnable = value

    @property    
    def on_select_all(self)->None:
        return None
    @on_select_all.setter
    def on_select_all(self,value):
        self.__on_select_all = value

    @property    
    def on_delete_from_group(self)->None:
        return None
    @on_delete_from_group.setter
    def on_delete_from_group(self,value):
        self.__on_delete_from_group = value

    def __init__(self,parent_widget):
        super().__init__(parent_widget)
        self.__onEnable = None
        self.__on_select_all = None
        self.__on_delete_from_group = None
        self.createUI()  
         

    def createUI(self):
        packSide(Button(self,text = __("settings"),command=self.__handleEnable))
        packSide(Button(self,text = __("select all"),command=self.__handleDisable))
        packSide(Button(self,text = __("delete from group"),command=self.__handleClear))
        packSide(Button(self,text = __("create Arduino"),command=self.__open_arduino_designer))

    def __open_arduino_designer(self):
        if self.__designer is not None:
          self.__designer.lift()
          self.__designer.focus()
          return
        self.__designer = Toplevel()
        ArduinoDesigner(self.__designer)
        self.__designer.protocol("WM_DELETE_WINDOW",self.__handle_close_designer)
        self.__designer.mainloop()
        pass

    def __handle_close_designer(self):
      self.__designer.destroy()
      self.__designer = None
      pass

    def __handleEnable(self):
        if callable(self.__onEnable):
            self.__onEnable()
        pass

    def __handleDisable(self):
        if callable(self.__on_select_all):
            self.__on_select_all()
        pass

    def __handleClear(self):
        if callable(self.__on_delete_from_group):
            self.__on_delete_from_group()
        pass

    __designer:Tk = None



