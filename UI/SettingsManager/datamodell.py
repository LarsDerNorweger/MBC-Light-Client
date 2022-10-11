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

class Arduino:
  pins:int
  typ:str
  def __init__(self,type,pins):
    self.pins = pins
    self.typ = type

  @property
  def __dict__(self):
    return{"pins":self.pins, "type":self.typ}


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
    pass

  @property
  def arduino(self)-> Arduino| None:
    return self.__arduino

  @arduino.setter
  def arduino(self, value:Arduino):
    self.__arduino = value
    pass

  def __init__(self,path:str):
    self.__path = path
    self.__load_settings()
    pass

  def save_settings(self):
    with open(self.__path,"w+") as fs:
        fs.write(json.dumps(self.__dict__))
    pass

  def __load_settings(self):
    try:
      with open(self.__path) as fs:
        set = json.loads(" ".join(fs.readlines()))
        self.__language = Language(set["language"]["speech"], set["language"]["path"])
        ard = Arduino(set["arduino"]["type"], set["arduino"]["pins"]) if set["arduino"] is not None else None
        self.__arduino = ard
    except:
      self.save_settings()    
    pass

  @property
  def __dict__(self):
    ard = self.arduino.__dict__ if self.arduino is not None else None
    return {"language":self.__language.__dict__,"arduino":ard}

  __language:Language = Language('english', '')
  __arduino = None