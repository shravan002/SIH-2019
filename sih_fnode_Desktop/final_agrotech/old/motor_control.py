
import pymysql
import RPi.GPIO as GPIO
import time

GPIO.setmode(GPIO.BCM)

pinlist = 17

GPIO.setup(pinlist,GPIO.OUT)

##to read parsed weather data
list = []
count = 0
rain = 0

try:
	f = open('/home/pi/parsed_weather_data.txt','r')
except IOError:
	print ("Error Occured")
	exit(0)
str = f.read()
list = str.split(",")
#print(list)
for l in list:
	if l == "Rain":
		count+=1

if count >=4:
	rain = 1;
#	print("rain")
else:
	rain = 0;
#	print("no rain")

##to read database

sm_thershold = 50
wl_thershold = 500

#mySQLconnection = pymysql.connect(host='localhost',database='smartlab',user='pi',password='lunatics@92',unix_socket='/var/run/mysqld/mysqld.sock')
#query = "select sm,wl from sensor_values order by timestamp desc"
#cursor.execute(query)
#records = cursor.fetchone()

records1 = 100
records2 = 300
if (float(records1) >= sm_thershold and float(records2) <= wl_thershold and rain == 1) :
	print("Inside motor control loop")
	GPIO.output(17,GPIO.LOW)
	while True:
		time.sleep(3)
		#cursor.execute(query)
		#records = cursor.fetchone()
		recordsss1 = 30
		recordsss2 = 600
		if (float(recordsss1) < sm_thershold and recordsss2 > wl_thershold) :
			print("Inside motor off loop")
			GPIO.output(17,GPIO.HIGH)
			break

#mySQLconnection.commit()
print("clean up toh ho gya")
GPIO.cleanup(pinlist)
print("done")
