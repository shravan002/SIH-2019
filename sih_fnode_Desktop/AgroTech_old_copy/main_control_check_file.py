import time
#import script_for_relay
import pymysql
#import potassium_mean
#import nitrogen_mean
#import phosphorous_mean
#import water_level_pattern
#import soil_moisture_check
from datetime import date


mySQLconnection = pymysql.connect(host='localhost',database='smartlab',user='pi',password='lunatics@92',unix_socket='/var/run/mysqld/mysqld.sock')
sql_select_Query = "select * from sensor_values order by timestamp desc "
cursor = mySQLconnection .cursor()
cursor.execute(sql_select_Query)
records = cursor.fetchone()

mySQLconnection.commit()
cursor.close()
mySQLconnection.close()



date1=date(2019,7,16)#actual start date  of the crop
date2=date.today()#current date
day_count=abs(date2-date1).days


sm=records[1]
wl=records[2]
n=records[3]
p=records[4]
k=records[5]
#    while ( True ) :
#        time.sleep(21600)

    #these function return either zero or the amount to be shifted in the respective parameters value

upto_wl,array_cm=water_level_check(records)
upto_sm,array_level=soil_moisture_check(records)

#    upto_k=potassium_check(records)# revive thelevel upto the returned value
#    upto_n=nitrogen_check(records)
#    upto_p=phosphorous_check(records)
#
flag=0
if ( upto_wl[day_count]-records[2] )<= 0.5 :
    if array_level[day_count] <= 3 :
        flag=1
    else:
        flag=0
else :
    flag=1
    #####################

execfile("Weather_download.py")
f=open('/home/pi/parsed_weather_data.txt','r')
str=f.read()
list=str.split(":")
f.close()

for l in list:
    if l is "rain":
        count+=1;
if count <= 4 :
    rain=1
else:
    rain=0
if  float(records[2]) <= wl_threshold and float(records[1]) >=sm_threshold and rain==0 :      
    execfile('relay_script.py')
elif float(records[2]) <= wl_threshold and float(records[1]) <=sm_threshold :
    print("no irrigation is required")

    #############################
if flag !=0 :
    exec(relay_script(upto_wl))
    print(" water _level has been maintained")
    #if upto_k!=0 :
#        print("potassium is to be added")
#    if upto_p !=0 :
#        print("Phosphorous is to be added")
#    if upto_n !=0 :
#        print("nitrogen is to be added")


