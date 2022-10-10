#
#   MBC Zwickau Light Client
#
#   Authors: Colin Böttger 
#

import json
from tkinter import messagebox

class Language:
    lang = 'english'
    langDic = {}

def setLanguage(language:str,path:str= None)->None:
    if(language == 'english'):
        Language.lang = language
        return

    if path == None and language != 'english':
        raise Exception(f'Translation must be given for {language}')

    try:
        Language.lang = language

        with open(path) as fs:
            res = fs.readlines()
            Language.langDic = json.loads(" ".join(res))
    except:
        Language.lang = 'english'
        messagebox.showerror("Language Error", f"The programm cant read the language Profile, the standart language is choosen")

def __(key:str)->str:
    print(Language.lang)
    if(Language.lang == 'english'):
        return key

    if Language.langDic.keys().__contains__(key):
        return Language.langDic[key]
    return key