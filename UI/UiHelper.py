#
#   MBC Zwickau Light Client
#
#   Authors: Colin Böttger 
#

def packDown(elem):
    elem.pack()
    return elem

def packSide(elem):
    elem.pack(side = "left")
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
      r = startvalue;
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
