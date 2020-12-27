import serial
import time

ser=serial.Serial('/dev/ttyUSB0',9600,timeout=1)#9600 is the default Baurdrate for SIM900A modem
ser.flush()
ser.write('ATD9459082453;\r')
#ser.read(2)
time.sleep(10)
ser.close()
