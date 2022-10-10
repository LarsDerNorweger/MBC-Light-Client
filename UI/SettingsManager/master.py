#
#   MBC Zwickau Light Client
#
#   Authors: Colin Böttger 
#

from tkinter import *
import json

from UI.translation import __
from UI.UiHelper import getPath
from UI.SettingsManager.datamodell import Language, Settings,Reload
from UI.SettingsManager.LanguageSelectorInterface import LanguageSelector


class SettingsManager(Frame):
    def __init__(self,master:Tk):
        super().__init__(master)
        master.title(__("settings"))
        self.settings = Settings(getPath("./UI/Settings/settings.json"))
        self.create_UI()
        self.pack()
        pass

    def create_UI(self):
      Label(self,text=__("settings")).pack()
      self.__lang_select=LanguageSelector(self, self.settings)
      self.__lang_select.pack()
      Button(self,text=__("Save"),command=self.__on_save).pack()
      Button(self,text=__("Cancle"),command=lambda:self.master.destroy()).pack()
      pass
    def set_language(self):

      pass

    def __on_save(self):
      self.settings.language = self.__lang_select.selected_lang
      self.master.destroy()
      raise Reload()
      pass

    __lang_select:LanguageSelector
 





