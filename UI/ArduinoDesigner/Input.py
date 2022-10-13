#
#   MBC Zwickau Light Client
#
#   Authors: Colin Böttger 
#

from tkinter import *

from UI.translation import __
from datamodell import Arduino

from UI.UiHelper import grid

class ArduinoInput(Frame):
    
    @property
    def arduino(self)->Arduino:
        return Arduino(self.__name_input.get(),ArduinoInput.__parse_input_to_Lists(self.__pin_input.get()))

    def __init__(self,master:Frame):
        super().__init__(master)
        self.createUI()
        pass

    def createUI(self):
        grid(Label(self,text=__("name")),0,1)
        self.__name_input = grid(Entry(self),0,2)

        grid(Label(self,text=__("pins")),1,1)
        self.__pin_input = grid(Entry(self),1,2)


        pass

    @staticmethod
    def __parse_input_to_Lists(inp:str):
        res = []
        if inp == '':
          return res

        parse = inp.split(',')
        for st in parse:
            if st.__contains__('-'):
                x = st.split('-')
                res.extend(range(int(x[0]),int(x[1])+1))
            else: res.append(int(st))
            pass
        res.sort()
        return res

    @staticmethod
    def __generat_partial_List(start:int, stop :int):
        res = []
        for i in range(start,stop):
            res.append(i)
        return res