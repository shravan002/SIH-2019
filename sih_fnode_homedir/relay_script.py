#!/usr/bin/python
import RPi.GPIO as GPIO
import time

GPIO.setmode(GPIO.BCM)

# init list with pin numbers

pinList = [17]

# loop through pins and set mode and state to 'high'

for i in pinList: 
    GPIO.setup(i, GPIO.OUT) 
    GPIO.output(i, GPIO.HIGH)

# time to sleep between operations in the main loop

SleepTimes = 5.0

# main loop

try:
  while True:

    for i in pinList:
      GPIO.output(i, GPIO.LOW)
      time.sleep(SleepTimes);
	
    for i in pinList:
      GPIO.output(i, GPIO.HIGH)
      time.sleep(SleepTimes);
      #print("enterted");
      
    pinList.reverse()

# End program cleanly with keyboard
except KeyboardInterrupt:
  print("quit");
  # Reset GPIO settings
  GPIO.cleanup()
