#!/usr/bin/python

import RPi.GPIO as GPIO
import time

GPIO.setmode(GPIO.BCM)

# init list with pin numbers

pinList = 17

# loop through pins and set mode and state to 'high'

GPIO.setup(pinList, GPIO.OUT)
GPIO.output(pinList, GPIO.HIGH)

# time to sleep between operations in the main loop

SleepTimes =3.0

# main loop
count=0
try:
  while True:
      if count % 2 == 0:
          GPIO.output(pinList, GPIO.HIGH)
      time.sleep(SleepTimes)
      if count % 2 != 0:
          GPIO.output(pinList, GPIO.LOW)
      count=count+1


# End program cleanly with keyboard
except KeyboardInterrupt:
  print("quit");
  # Reset GPIO settings
  GPIO.cleanup()
