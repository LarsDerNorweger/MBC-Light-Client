#
#   MBC Zwickau Light Client
#
#   Authors: Colin Böttger 
#

from tkinter import *
from tkinter import filedialog
from tkinter import messagebox
from UI.UiHelper import packSide
from UI.translation import __

FILETYPE =     (
        ('lux files', '*.lux'),
        ('All files', '*.*')
    )

class SaveProfileInterface(Frame):
    def __init__(self,master):
        super().__init__(master)
        self.__create_ui()
        pass

    def __create_ui(self):
        packSide(Button(self,text=__("Save profile"),command=self.__handle_safe))
        packSide(Button(self,text=__("Load profile"),command=self.__handle_load))
        pass

    def __handle_safe(self):
        filename = filedialog.askopenfilename(title=__("Save Path"),initialdir='/',filetypes=FILETYPE)
        messagebox.showinfo('',filename)
        pass

    def __handle_load(self):
        pass