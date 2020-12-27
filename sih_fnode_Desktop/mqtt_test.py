import paho.mqtt.client as mqttClient
import time
import pymysql

def on_connect(client, userdata, flags, rc):
    if rc == 0:
        print("Connected to broker")
        global Connected                #Use global variable
        Connected = True                #Signal connection
    else:
        print("Connection failed")

def on_message(client, userdata, message):
    print("Test message")
    print("Message received: "  + str(message.payload.decode("utf-8")))
    sql = "insert into soil_moisture(value) values(%s)"
    cursor.execute(sql,str(message.payload.decode("utf-8")))
    print("after inserting db record")

Connected = False   #global variable for the state of the connection

broker_address= "192.168.0.8"  	#Broker address
port = 1883                     #Broker port
user = "rsraju"                 #Connection username
password = "18mcpc13"           #Connection password

db = pymysql.connect("localhost","pi","openhabiann","SmartLab")
cursor = db.cursor()

client = mqttClient.Client("Python")               #create new instance
client.username_pw_set(user, password=password)    #set username and password
client.on_connect= on_connect                      #attach function to callback
client.on_message= on_message                      #attach function to callback

client.connect(broker_address, port=port)          #connect to broker

client.loop_start()        #start the loop

while Connected != True:    #Wait for connection
    time.sleep(1)

client.subscribe("esp8266")

try:
    while True:
        time.sleep(1)

except KeyboardInterrupt:
    print("exiting")
    db.commit()
    db.close()
    client.disconnect()
    client.loop_stop()
