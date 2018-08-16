import os
import time
import Rpi.GPIO as GPIO

class LED:
 

 def lit(self,prob):
 
  GPIO.setmode(GPIO.BOARD)
  GPIO.setup(4,GPIO.OUT)
  if prob>0.5:
   GPIO.output(4,GPIO.HIGH)
   time.sleep(5)
  else:
   GPIO.output(4,GPIO.LOW)
   time.sleep(5)
GPIO.cleanup()
