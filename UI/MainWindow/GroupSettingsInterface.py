#
#   MBC Zwickau Light Client
#
#   Authors: Colin Böttger 
#

from tkinter import *

from datamodell import Group
from UI.UiHelper import grid
from UI.translation import __

class GroupSettingsInterface(Frame):
    @property
    def group(self)->Group:
        return self.__displayed_group

    @group.setter
    def group(self,value:Group):
        if self.__displayed_group:
            self.__displayed_group.name = self.__name.get()
            d = float(self.__delay.get().replace(',','.') )
            self.__displayed_group.delay = d if d>0 else None
        
        self.__displayed_group = value
        self.__name.delete(0,END)
        self.__name.insert(0,value.name)
        self.__delay.delete(0,END)
        self.__delay.insert(0,str(value.delay if value.delay else 0))

    def __init__(self,master):
        super().__init__(master)
        self.__displayed_group = None
        self.__create_UI()
        pass

    def __create_UI(self):
        grid(Label(self,text=__("Group settings")),1,1,2)
        
        grid(Label(self,text=__("name")+':'),2,1)
        self.__name = grid(Entry(self),2,2)
        
        grid(Label(self,text=__("delay in sek")+':'),3,1)
        self.__delay = grid(Entry(self),3,2)
        pass

    __displayed_group:Group

    __name:Entry
    __delay:Entry
