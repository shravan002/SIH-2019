import RPi.GPIO as GPIO
import time

GPIO.setmode(GPIO.BCM)


pinlist = 17

GPIO.setup(pinlist,GPIO.OUT)
#GPIO.cleanup()
GPIO.output(pinlist. GPIO.HIGH)


GPIO.cleanup(pinlist)
