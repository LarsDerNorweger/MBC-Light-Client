#
#   MBC Zwickau Light Client
#
#   Authors: Colin Böttger 
#

import json
global lang

class Language:
    lang = 'en'
    langDic = {}


def setLanguage(language:str,path:str= None):
    if(language == 'en'):
        Language.lang == 'en'
        return

    if path == None and language != 'en':
        raise Exception(f'Translation must be given for {language}')

    Language.lang = language

    with open(path) as fs:
        res = fs.readlines()
        Language.langDic = json.loads(convertStringArrayToString(res))

def convertStringArrayToString(arr):
    res = ''
    for i in arr:
        res+=i
    return res


def __(key:str):
    if(Language.lang == 'en'):
        return key

    if Language.langDic.keys().__contains__(key):
        return Language.langDic[key]
    return key