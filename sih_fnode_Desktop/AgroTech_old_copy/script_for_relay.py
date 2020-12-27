import RPi.GPIO as GPIO
import time

GPIO.setmode(GPIO.BCM)

# init list with pin numbers

pinList = [17]

# loop through pinsmport RPi.GPIO as GPIO
import time

GPIO.setmode(GPIO.BCM)

# init list with pin numbers

pinList = [17]

# loop through pins and set mode and state to 'high'

for i in pinList: 
    GPIO.setup(i, GPIO.OUT) 
    GPIO.output(i, GPIO.HIGH)

# time to sleep between operations in the main loop

SleepTimes =5

# main loop

try:
  while True:
    GPIO.output(pinList[0], GPIO.LOW)
    time.sleep(SleepTimes)
    GPIO.output(pinList[0], GPIO.HIGH)
    time.sleep(SleepTimes);

# End program cleanly with keyboard
except KeyboardInterrupt:
  print("quit");
  # Reset GPIO settings
  GPIO.cleanup()
 
