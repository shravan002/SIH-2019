
import time
import os
import motor_control as motor
import pymysql
import potassium_mean as potas
import nitrogen_mean as nitro
import phosphorous_mean as phospho
import water_level_pattern as water
import soil_moisture_check as moisture
from datetime import date
import Weather_download
import weather_data_parsing

print("1")

mySQLconnection = pymysql.connect(host='localhost',database='smartlab',user='pi',password='lunatics@92',unix_socket='/var/run/mysqld/mysqld.sock')
sql_select_Query = "select * from sensor_values order by timestamp desc "
cursor = mySQLconnection .cursor()
cursor.execute(sql_select_Query)
records = cursor.fetchone()

mySQLconnection.commit()
cursor.close()
mySQLconnection.close()

print("2")

date1=date(2019,7,16)#actual start date  of the crop
date2=date.today()#current date
day_count=abs(date2-date1).days
print("3")

sm=int(records[1])
wl=int(records[2])
n=float(records[3])
p=float(records[4])
k=float(records[5])
print(sm,wl,n,p,k)

#these function return either zero or the amount to be shifted in the respective parameters value
#currently not using array_cm


upto_wl,array_cm=water.water_level_check(records)
upto_sm,sm_level=moisture.soil_moisture_check(records)
upto_n=nitro.nitrogen_check(n)
upto_p=phospho.phosphorous_check(p)
upto_k=potas.potassium_check(k)

print("4")
#####################
"""WEATHER NOTIFICATION"""


t=exec(open('Weather_download.py').read())
f=open('parsed_weather_data.txt','r')
str=f.read()
list=str.split(":")
f.close()



for l in list:
    if l =="Rain":
        count+=1;

if count <= 4 :
    rain=0
else:
    rain=1
print(rain,count)
print()
print(sm,wl,n,k)
print()
print(upto_sm,upto_wl)

if  float(wl) <= upto_wl and rain==0 :
    flag=1
    #if (( upto_wl-wl )<= 0.5 ):
    #    if (int(sm_level) <= 3) :
    #        flag=1
    #    else:
    #       flag=0
    #else :
    #    flag=1
    print("irrigation  %d  "%(flag))
    if flag ==1 :
        motor.motor_control(upto_wl,upto_sm)
        print(" water _level has been maintained")
        print("6")

elif float(wl) <= upto_wl and float(sm) <= upto_sm :
   if(rain == 0):
        print("no irrigation is required")
   else:
        print("Rain is expected so do not irrigate ")
#motor.motor_control(upto_wl,upto_sm)

print("7")

