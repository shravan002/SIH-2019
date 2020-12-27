import paho.mqtt.client as mqttClient
import time
import datetime
import pymysql

def on_message(client, userdata, message):
    print("Inside on_message function")
    print("Message received: "  + str(message.payload.decode("utf-8")))

    sql = "insert into sensor_values(timestamp,sm,wl,n,p,k) values(%s,%s,%s,%s,%s,%s)"

    msg = str(message.payload.decode("utf-8"))
    sensor_values = msg.split(":")
    sm = sensor_values[0]
    wl = sensor_values[1]
    n = sensor_values[2]
    p = sensor_values[3]
    k = sensor_values[4]
    timestamp = str(datetime.datetime.now())
    timestamp = timestamp[0:19]
    tuple = (timestamp,sm,wl,n,p,k)
    print(tuple)
    try:
        cursor.execute(sql,tuple)
        db.commit()
        #sleep(20000)
    except e:
        print("exception has come")

    print("after inserting db record")


broker_address= "192.168.0.5"   #Broker address
port = 1883                     #Broker port

db = pymysql.connect(db="smartlab", user="pi", passwd="lunatics@92",unix_socket="/var/run/mysqld/mysqld.sock")

cursor = db.cursor()

client = mqttClient.Client("edgenode")               #create new instance
client.on_message= on_message                      #attach function to callback
client.connect(broker_address, port=port)          #connect to broker
#print("Connection established")

client.loop_start()        #start the loop
#print("After loop start statement")
client.subscribe("esp8266")
#print("After subscribe")

try:
    while True:
        time.sleep(60)


except KeyboardInterrupt:
    print("exiting..")
    db.close()
    client.disconnect()
    client.loop_stop()


