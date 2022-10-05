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

class Tools(Frame):

    @property    
    def onPinEnable(self)->None:
        return None
    @onPinEnable.setter
    def onPinEnable(self,value):
        self.__onEnable = value

    @property    
    def onPinDisable(self)->None:
        return None
    @onPinDisable.setter
    def onPinDisable(self,value):
        self.__onDisable = value

    @property    
    def onClear(self)->None:
        return None
    @onClear.setter
    def onClear(self,value):
        self.__onClear = value

    def __init__(self,parent):
        super().__init__(parent)
        self.__onEnable = None
        self.__onDisable = None
        self.__onClear = None
        self.createUI()    

    def createUI(self):
        packSide(Button(self,text = __("enable pin"),command=self.__handleEnable))
        packSide(Button(self,text = __("disable pin"),command=self.__handleDisable))
        packSide(Button(self,text = __("clear selection"),command=self.__handleClear))

    def __handleEnable(self):
        if callable(self.__onEnable):
            self.__onEnable()
        pass

    def __handleDisable(self):
        if callable(self.__onDisable):
            self.__onDisable()
        pass

    def __handleClear(self):
        if callable(self.__onClear):
            self.__onClear()
        pass




