#
#   MBC Zwickau Light Client
#
#   Authors: Colin Böttger 
#

import json

from tkinter import *
from tkinter import ttk
from UI.UiHelper import getPath

from UI.UiHelper import packSide
from UI.translation import __


from UI.SettingsManager.datamodell import Language

from UI.translation import __
class Chache():
  languages = None


class LanguageSelector(Frame):
    @property
    def selected_lang(self)->Language:
      lang = self.__selected_lang.get()
      return Language(lang, Chache.languages[lang])

    def __init__(self,master:Tk,settings):
        super().__init__(master)
        self.load_languages()
        self.__selected_lang = StringVar(self,value=settings.language.speech)
        self.create_UI()
        pass

    def create_UI(self):
      packSide(Label(self,text=__("language")+' :'))
      cb = packSide(ttk.Combobox(self,textvariable=self.__selected_lang))
      keys = []
      for i in Chache.languages.keys():
        keys.append(i)
      cb["values"]=keys
      pass

    def load_languages(self):
      if Chache.languages is not None:
        return
      try:
        with open(getPath("languages/support.json")) as fs:
          Chache.languages = json.loads("".join(fs.readlines()))
          Chache.languages["english"]=''
        pass
      except Exception as e:
        Chache.languages = {"english":''}
        pass
      pass