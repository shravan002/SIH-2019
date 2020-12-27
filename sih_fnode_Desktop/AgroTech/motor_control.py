

import pymysql
import RPi.GPIO as GPIO
import time


def motor_control(upto_wl,upto_sm):
     try:
        GPIO.setmode(GPIO.BCM)
        pinlist = 17
        GPIO.setup(pinlist,GPIO.OUT)
        GPIO.output(pinlist,GPIO.LOW)
        sm_thershold = upto_sm
        wl_thershold = upto_wl

        mySQLconnection = pymysql.connect(host='localhost',database='smartlab',user='pi',password='lunatics@92',unix_socket='/var/run/mysqld/mysqld.sock')
        query = "select sm,wl from sensor_values order by timestamp desc"
        cursor=mySQLconnection.cursor()
        cursor.execute(query)
        records = cursor.fetchone()
        print("    sm,    wl")
        print(upto_sm,upto_wl)
        print(records)
        #if (float(records[0]) >= sm_thershold and float(records[1]) <= wl_thershold):
        if True:
            print("Inside motor control loop")
            GPIO.output(17,GPIO.LOW)
            while True:
                time.sleep(2)
                cursor.execute(query)
                records_1 = cursor.fetchone()
                print("new record taken")
                if (float(records_1[0]) < sm_thershold and float(records_1[1]) > wl_thershold):
                    print("Inside motor off loop")
                    GPIO.output(pinlist,GPIO.HIGH)
                    break
        mySQLconnection.commit()
        cursor.close()
        mySQLconnection.close()

     except KeyboardInterrupt:
         print("quit");
         # Reset GPIO settings
         GPIO.cleanup()
motor_control(124,765)

