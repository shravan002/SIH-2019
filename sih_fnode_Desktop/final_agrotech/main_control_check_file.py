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
#import weather_data_parsing
import send_notification as sms

while True:
    try:
        #print("check 0")
        mySQLconnection = pymysql.connect(host='localhost',database='smartlab',user='pi',password='lunatics@92',unix_socket='/var/run/mysqld/mysqld.sock')
        sql_select_Query = "select * from sensor_values order by timestamp desc "
        cursor = mySQLconnection .cursor()
        cursor.execute(sql_select_Query)
        records = cursor.fetchone()
    except (KeyboardInterrupt,ImportError,IOError) as e:
        mySQLconnection.commit()
        cursor.close()
        mySQLconnection.close()
    
    date1=date(2019,7,29)#actual start date  of the crop
    date2=date.today()#current date
    day_count=abs(date2-date1).days
    #print("1")

    sm=int(records[1])
    wl=int(records[2])
    nitrogen=float(records[3])
    phosphorous=float(records[4])
    potassium=float(records[5])
    print("\n-------------------------------")
    print("Soil moisture :%d\nWater Level :%d\nNitrogen :%f\nPhosphorous %f\nPotassium %f"%(sm,wl,nitrogen,phosphorous,potassium))
    print("-------------------------------")
    
    #these function return either zero or the amount to be shifted in the respective parameters value
    #currently not using array_cm

    

    upto_wl,array_cm=water.water_level_check(wl)
    upto_sm,sm_level,sm_mean=moisture.soil_moisture_check(sm)
    #print(upto_sm)
    upto_n=nitro.nitrogen_check(nitrogen)
    upto_p=phospho.phosphorous_check(phosphorous)
    upto_k=potas.potassium_check(potassium)
    

    if(upto_sm==0):
        upto_sm=sm_mean
    if(upto_wl==0):
        upto_wl=wl_mean
        

    print("Required Level:\n-------------------------------------------\nSoil_moisture %d| Water level %d\n-------------------------------------------\n"%(int(upto_sm),int(upto_wl)))
    print("\nCurrent Level:\n--------------------------------------------\nSoil_moisture %d| Water level %d\n-------------------------------------------\n"%(int(sm),int(wl)))
    #####################
    """WEATHER NOTIFICATION"""

    #t=exec(open('Weather_download.py').read())
    #f=open('parsed_weather_data.txt','r')
    #str=f.read()
    #list=str.split(",")
    #f.close()
    
    count=0
    aggregate=0
    #for i in range(16):
    #    if list[i] =="Rain":
    #        count+=1;
    #        if(i<4):
    #            k=(16-i)
    #        elif(i<8):
    #            k=12-i
    #        elif(i<12):
    #            k=4
    #        else:
    #            k=3
    #        aggregate=aggregate+k
            
    aggregate=25
    if aggregate <= 30 :
        rain=0
    else:
        rain=1
    rain=0
    #print("check 4   =   %f %f"%(rain,count))
    
    #if(upto_sm==0):
    #    upto_sm=sm
    #print(float(sm))
    #print(float(upto_sm))
    
    if (float(wl) <= upto_wl and float(sm) >= upto_sm) :
       if(rain == 0):
            #print("check 5")
            print("##########################################")
            print("\nIrrigation is required")
            print("------------------------------------------")
            print("Water pump has been turned ON")
            
            try:
                motor.motor_control(upto_wl,upto_sm)
            except KeyboardInterrupt:
                print("Keyboard Interrupt!!!")
                exit(0)
            #print("check 6")
            
            sms.notification(2,"Water pump has been turned ON")
            #print("check 7")
            print("------------------------------------------")
            print("Water _level has been maintained")
            print("------------------------------------------")
            print("Next iteration will be after 6hrs")
            print("##########################################")
            
       else:
            #print("check 7")
            print("------------------------------------------")
            print("Rain is expected so do not irrigate ")
            print("------------------------------------------")
            print("Next iteration will be after 6hrs")
            print("------------------------------------------") 
    else :
          print("------------------------------------------")
          print("NO IRRIGATION IS REQUIRED")
          print("------------------------------------------")
    #print("check 8")
    
    try:
       time.sleep(60)
    except KeyboardInterrupt:
       print("keyboard input for Quit")
       exit(0)
