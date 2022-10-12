#
#   MBC Zwickau Light Client
#
#   Authors: Colin Böttger 
#

from tkinter import *

from UI.translation import __
from UI.UiHelper import grid
from defines import DEFINES
from UI.SettingsManager.datamodell import Settings,Reload
from UI.SettingsManager.LanguageSelectorInterface import LanguageSelector
from UI.SettingsManager.ArduinoSelectionInterface import ArduinoSelectionInterface


class SettingsManager(Frame):
    def __init__(self,master:Tk):
        super().__init__(master)
        master.title(__("settings"))
        self.onclose = None
        self.master = master
        master.report_callback_exception = self.__handle_error
        self.settings = Settings(DEFINES.SETTINGS)
        self.create_UI()
        self.pack()
        self.master.protocol("WM_DELETE_WINDOW",self.__on_cancle)
        
        pass

    def __handle_error(self,esc,val,tb):
      raise val

    def create_UI(self):
      grid(Label(self,text=__("settings"),font=(10)),0,0,columnspan=2)
      self.__lang_select=grid(LanguageSelector(self, self.settings),1,0,columnspan=2)

      self.__arduino_select = grid(ArduinoSelectionInterface(self,self.settings),2,0,columnspan=2)
      
      grid(Button(self,text=__("Save"),command=self.__on_save),3,0)
      grid(Button(self,text=__("Cancle"),command=self.__on_cancle),3,1)
      pass
    
    def __on_cancle(self):
        if callable(self.onclose):
          self.onclose()

    def __on_save(self):
      self.settings.language = self.__lang_select.selected_lang
      self.settings.arduino = self.__arduino_select.selected_arduino
      self.settings.save_settings()
      self.master.destroy()
      raise Reload()


    __lang_select:LanguageSelector
 





