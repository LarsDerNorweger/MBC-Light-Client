#
#   MBC Zwickau Light Client
#
#   Authors: Colin Böttger 
#

import json
import pathlib

from tkinter import *
from tkinter import filedialog
from tkinter import messagebox

from datamodell import Group
from UI.UiHelper import packSide
from UI.translation import __

FILETYPE =     (
        ('lux files', '*.lux'),
        ('All files', '*.*')
    )
HOME = str(pathlib.Path.home())

class SaveProfileInterface(Frame):

    @property
    def on_save(self)->None:
        return None
    @on_save.setter
    def on_save(self,value):
        self.__on_save = value


    @property
    def on_load(self)->None:
        return None
    @on_load.setter
    def on_load(self,value):
        self.__on_load = value

    def __init__(self,master):
        super().__init__(master)
        self.__create_ui()
        self.__on_load = None
        self.__on_save = None
        pass

    def __create_ui(self):
        packSide(Button(self,text=__("Save profile"),command=self.__handle_safe))
        packSide(Button(self,text=__("Load profile"),command=self.__handle_load))
        pass

    def __handle_safe(self):
        filename = filedialog.asksaveasfilename(title=__("Save Path"), initialdir=HOME,defaultextension='lux',initialfile="mbcLightConfig")
        if(filename == ''):
            return
        
        profile = None
        if callable(self.__on_save):
            profile = self.__on_save()
        if profile is None:
            raise Exception(__("no handler installed"))
        save_profile(filename, profile)
        pass

    def __handle_load(self):
        filename = filedialog.askopenfilename(title=__("Save Path"),initialdir=HOME,filetypes=FILETYPE)
        if filename == '':
            return

        res  = load_profile(filename)
        if callable(self.__on_load) and res is not None :
            self.__on_load(res)
        pass

class encoder(json.JSONEncoder):
    def default(self, o):
        if isinstance(o,Group):
            return o.__dict__
        return super().default(o)

def save_profile(path:str, profile):
    try:
        with open(path,"+w") as fs:
            fs.write(encoder().encode(profile))
            pass    
        pass
    except EOFError:
        messagebox.showerror(__("An error occured"),__("failed to load file")+' '+path)
        pass
    except json.JSONDecodeError:
        messagebox.showerror(__("An error occured"),__("failed to parse file")+' '+path)
        pass
    pass

def load_profile(path:str):
    res = None
    try:
        with open(path) as fs:
            res = json.loads(''.join(fs.readlines()))
            pass    
        pass
    except EOFError:
        messagebox.showerror(__("An error occured"),__("failed to load file")+' '+path)
        pass
    except json.JSONDecodeError:
        messagebox.showerror(__("An error occured"),__("failed to parse file")+' '+path)
        pass
    return res