import paho.mqtt.client as mqttClient
import time
import datetime
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
    print("From:  " + str(client))
    #sql = "insert into soil_moisture(timestamp,value) values(%s,%s)"
    #tuple = (str(datetime.datetime.now()),str(message.payload.decode("utf-8")))
    #cursor.execute(sql,tuple)
    #db.commit()
    #print("after inserting db record")

Connected = False   #global variable for the state of the connection

broker_address= "10.5.0.124" #Broker address
port = 1883                     #Broker port
user = "pi"                     #Connection username
password = "lunatics@92"        #Connection password


#db = pymysql.connect("localhost","pi","lunatics@92","smartlab")
#cursor = db.cursor()

client = mqttClient.Client("Python")               #create new instance
client.username_pw_set(user, password=password)    #set username and password
client.on_connect= on_connect                      #attach function to callback
client.on_message= on_message                      #attach function to callback

client.connect(broker_address, port=port)          #connect to broker

client.loop_start()        #start the loop

while Connected != True:    #Wait for connection
    time.sleep(1)

client.subscribe("esp8266")


i = 0

try:
    while True:
        time.sleep(1)
        #x = 0

except KeyboardInterrupt:
    print("exiting")
    #db.commit()
    #db.close()
    client.disconnect()
    client.loop_stop()
