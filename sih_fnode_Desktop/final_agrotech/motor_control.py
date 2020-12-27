
import pymysql
import RPi.GPIO as GPIO
import time


def motor_control(upto_wl,upto_sm):
     try:
        #GPIO.cleanup()
        GPIO.setmode(GPIO.BCM)
        pinlist = 17
        GPIO.setup(pinlist,GPIO.OUT)
        GPIO.output(pinlist,GPIO.LOW)
        sm_threshold = upto_sm
        wl_threshold = upto_wl
        
        mySQLconnection = pymysql.connect(host='localhost',database='smartlab',user='pi',password='lunatics@92',unix_socket='/var/run/mysqld/mysqld.sock')
        query = "select sm,wl from sensor_values order by timestamp desc"
        cursor=mySQLconnection.cursor()
        cursor.execute(query)
        records = cursor.fetchone()
        
        #mySQLconnection.commit()
        #cursor.close()
        #mySQLconnection.close()
        print("Required Level:\n-------------------------------------------\nSoil_moisture %d| Water level %d\n-------------------------------------------\n"%(int(sm_threshold),int(wl_threshold)))
        print("\nCurrent Level:\n--------------------------------------------\nSoil_moisture %d| Water level %d\n-------------------------------------------\n"%(int(records[0]),int(records[1])))
        #print(upto_sm,upto_wl)
        #print(records)
        
        if (float(records[0]) >= sm_threshold and float(records[1]) <= wl_threshold):
            print("Inside motor control loop")
            GPIO.output(17,GPIO.LOW)
            while True:
                time.sleep(25)
                mySQLconnection = pymysql.connect(host='localhost',database='smartlab',user='pi',password='lunatics@92',unix_socket='/var/run/mysqld/mysqld.sock')
                query = "select sm,wl from sensor_values order by timestamp desc"
                cursor=mySQLconnection.cursor()
                cursor.execute(query)
                records_1 = cursor.fetchone()
                print("--------------------------------")
                print("New records taken")
                print("\nSoil moisture =%f   Water level =%f"%(float(records_1[0]),float(records_1[1])))
                if (float(records_1[1]) > wl_threshold ):
                    print("--------------------------------")
                    print("Inside motor off loop")
                    print("--------------------------------")
                    GPIO.output(pinlist,GPIO.HIGH)
                    break
        mySQLconnection.commit()
        cursor.close()
        mySQLconnection.close()
        GPIO.cleanup()

     except KeyboardInterrupt:
         print("quit");
         # Reset GPIO settings
         GPIO.cleanup()
         exit(0)


#motor_control(800,150)
