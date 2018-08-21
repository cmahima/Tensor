import os
import time
import RPi.GPIO as GPIO

class LED:
 
 
 def lit(self,prob):
  i=3
  GPIO.setmode(GPIO.BOARD)
  GPIO.setwarnings(False)
  GPIO.setup(7,GPIO.OUT)
  print('Probability is ' +prob)
  while(i>0): 
   if float(prob)>0.5:
   # print('hi')
    
    GPIO.output(7,GPIO.HIGH)
    time.sleep(1)
    GPIO.output(7,GPIO.LOW)
    GPIO.output(7,GPIO.LOW)
    time.sleep(1)
    i-=1
   else:
    #print('hello')
    GPIO.output(7,GPIO.LOW)
    time.sleep(1)
    i-=1
  GPIO.output(7,GPIO.LOW)
  GPIO.cleanup()
