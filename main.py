import time
from Serial.SerialManager import SerialManager
import sys


def convertMessage(msg:str):
  return int(msg[0:len(msg)-2])


def t(this,x):
  msg = convertMessage(x)
  if msg == 2048:
    raise Exception("Unkown Command")
  if msg == 2049:
    raise Exception("Argument Exception")
  if msg == 4096:
    this.sendLine(next(p))
  if(msg == 1024):
    this.stop()


def setPin(pin,state,delay):
  yield str(0)
  yield str(pin)
  yield str(state)
  yield str(delay)

p = setPin(15,1,100)
s = SerialManager('COM10',t)


print("wait")
s.start()
s.sendLine(next(p))
time.sleep(5)
s.stop()
print("stop")
time.sleep(1)
print("end")