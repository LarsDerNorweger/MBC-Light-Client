#
#   MBC Zwickau Light Client
#
#   Authors: Colin Böttger 
#

import json
from UI.UiHelper import getPath

class Reload(Exception):
  def __init__(self):
    super().__init__()
    pass


class Language:
    speech:str
    path:str
    def __init__(self,speech,path):
      self.speech = speech
      self.path = path  
    
    @property
    def __dict__(self):
      return{"speech":self.speech,"path":self.path}


class Settings:
  @property
  def language(self):
    return self.__language

  @language.setter
  def language(self, value):
    self.__language = value
    self.__save_settings()
    pass

  def __init__(self,path:str):
    self.__path = path
    self.__load_settings()
    pass

  def __save_settings(self):
    with open(self.__path,"w+") as fs:
        fs.write(json.dumps(self.__dict__))
    pass

  def __load_settings(self):
    try:
      with open(self.__path) as fs:
        set = json.loads(" ".join(fs.readlines()))
        self.__language = Language(set["language"]["speech"], set["language"]["path"])
    except:
      self.__save_settings()    
    pass

  @property
  def __dict__(self):
    return {"language":self.__language.__dict__}

  __language:Language = Language('englisch', '')