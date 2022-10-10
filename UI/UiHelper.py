#
#   MBC Zwickau Light Client
#
#   Authors: Colin Böttger 
#

from typing import TypeVar

T = TypeVar('T')
def packDown(elem:T)->T:
    elem.pack(pady=1)
    return elem

def packSide(elem:T)->T:
    elem.pack(side = "left",padx=4)
    return elem

def grid(elem:T,x:int,y:int,columnspan = 1,rowspan=1,sticky = 'n') ->T:
  elem.grid(row = x, column = y,columnspan= columnspan,rowspan = rowspan,sticky=sticky)
  return elem


def WebsaveColorGenerator(startvalue = 0):
  startvalue = round(startvalue/51)
  startvalue = 51*startvalue
  r= startvalue
  g= startvalue
  b = startvalue
  while b<255:
    while g<255:
      while r<255:
        r+=51
        yield _from_rgb((r,g,b))
      r = startvalue
      g+=51
      yield _from_rgb((r,g,b))
    g =startvalue
    b+=51
    yield _from_rgb((r,g,b))
  pass


def _from_rgb(rgb):
    """translates an rgb tuple of int to a tkinter friendly color code
    """
    return "#%02x%02x%02x" % rgb 

def getPath(path):
  return path
