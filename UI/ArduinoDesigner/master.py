#
#   MBC Zwickau Light Client
#
#   Authors: Colin Böttger 
#

from defines import DEFINES

import json

from tkinter import *
from tkinter import messagebox
from UI.SettingsManager.datamodell import Reload

from UI.translation import __
from UI.UiHelper import grid
from UI.ArduinoDesigner.Input import ArduinoInput

class ArduinoDesigner(Frame):
    def __init__(self,master:Tk):
        super().__init__(master)
        self.load_arduinos()
        self.on_close = None
        master.protocol("WM_DELETE_WINDOW", self.__handle_close)
        self.master = master
        self.master.title(__("create Arduino"))
        self.createUI()
        self.pack()
        master.report_callback_exception = self.handleError
        pass

    def handleError(self,exc, val, tb):
      raise val

    def createUI(self):
        grid(Label(self,text = __("create Arduino")),0,0,columnspan=2)
        self.input = grid(ArduinoInput(self),1,0,columnspan=2)
        grid(Button(self,text=__("Save"),command=self.__handle_save),2,0)
        grid(Button(self,text=__("Cancle"),command=self.__handle_close),2,1)

    def __handle_save(self):
        print(self.input.arduino.__dict__)
        ard = self.input.arduino
        if callable(self.on_close):
            self.on_close()
        if(ard.typ == ""):
          return
          
        if self.check_override(ard.typ):
          self.Arduinos[ard.typ] = ard.pins
          self.save_arduinos()
          raise Reload
        return

    def __handle_close(self):
        if callable(self.on_close):
            self.on_close()

    def check_override(self,key):
      if not self.Arduinos.__contains__(key):
        return True
      return messagebox.askyesno(__("create Arduino"),f"{__('Do you want to override the arduino')}: {key}")

    def load_arduinos(self):
      self.Arduinos = {}
      try:
        with open(DEFINES.ARDUINO_PATH) as fs:
          res = ''.join(fs.readlines())
          self.Arduinos = json.loads(res)
          pass  
        pass
      except Exception as e:
        messagebox.showerror(__("an error occured"),e)
        self.save_arduinos()
        pass
      pass

    def save_arduinos(self):
      try:
        with open(DEFINES.ARDUINO_PATH,"w+") as fs:
          res = json.dumps(self.Arduinos)
          fs.write(res)
          pass  
        pass
      except Exception as e:
        messagebox.showerror(__("an error occured"),e)
        pass
      pass
      pass



    
    