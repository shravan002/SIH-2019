import paho.mqtt.client as mqttClient
import time
import datetime
import pymysql

def on_connect1(client, userdata, flags, rc):  # c1 - soil mositure
    if rc == 0:
        print("C1 - Connected to broker")
        global Connected1                #Use global variable
        Connected1 = True                #Signal connection
    else:
        print("C1 - Connection failed")

def on_connect2(client, userdata, flags, rc): #c2 - water level
    if rc == 0:
        print("C2 - Connected to broker")
        global Connected2                #Use global variable
        Connected2 = True                #Signal connection
    else:
        print("C2 - Connection failed")


def on_message1(client, userdata, message):
    print("Test message1")
    print("Message1 received from Soil Moisture Sensor: "  + str(message.payload.decode("utf-8")))
    print("From:  " + str(client))
    sql = "insert into sensor_values(parameter,timestamp,value) values(%s,%s,%s)"
    tuple = (str("sm"),str(datetime.datetime.now()),str(message.payload.decode("utf-8")))
    cursor.execute(sql,tuple)
    db.commit()
    print("after inserting db record")

def on_message2(client, userdata, message):
    print("Test message2")
    print("Message2 received from Water Level Sensor: "  + str(message.payload.decode("utf-8")))
    print("From:  " + str(client))
    sql = "insert into sensor_values(parameter,timestamp,value) values(%s,%s,%s)"
    tuple = (str("wl"),str(datetime.datetime.now()),str(message.payload.decode("utf-8")))
    cursor.execute(sql,tuple)
    db.commit()
    print("after inserting db record")

Connected1 = False   #global variable for the state of the connection
Connected2 = False

broker_address= "10.5.0.124" #Broker address
port = 1883                     #Broker port
user = "pi"                     #Connection username
password = "lunatics@92"        #Connection password


db = pymysql.connect("localhost","pi","lunatics@92","smartlab")
cursor = db.cursor()

client1 = mqttClient.Client("Python")               #create new instance
client1.username_pw_set(user, password=password)    #set username and password
client1.on_connect= on_connect1                      #attach function to callback
client1.on_message= on_message1                      #attach function to callback

client2 = mqttClient.Client("Python2")               #create new instance
client2.username_pw_set(user, password=password)    #set username and password
client2.on_connect= on_connect2                      #attach function to callback
client2.on_message= on_message2

client1.connect(broker_address, port=port)          #connect to broker
client2.connect(broker_address, port=port)

client1.loop_start()                        #start the loop
client2.loop_start()

while Connected1 != True and Connected2 != True:    #Wait for connection
    time.sleep(1)

client1.subscribe("esp8266")
client2.subscribe("waterlevel")

client1.loop_start()
client2.loop_start()

try:
    while True:
        time.sleep(1)

except KeyboardInterrupt:
    print("exiting")
    #db.commit()
    db.close()
    client1.disconnect()
    client1.loop_stop()
    client2.disconnect()
    client2.loop_stop()
