import paho.mqtt.client as mqttClient
import time
import datetime
import pymysql

def on_connect(client, userdata, flags, rc):
    if rc == 0:
        print("Connected to broker")
        global Connected                #Use global variable
        Connected = True                #Signal connection
        client.subscribe("esp8266")
        print("Client Subscribed")
        time.sleep(10)
    else:
        print("Connection failed")


Connected = False   		#global variable for the state of the connection

broker_address= "192.168.0.5"   #Broker address
port = 1883                     #Broker port
user = "pi"                     #Connection username
password = "lunatics@92"        #Connection password

client = mqttClient.Client(client_id="Python",clean_session=False)               #create new instance
client.username_pw_set(user, password=password)    #set username and password
client.on_connect= on_connect                      #attach function to callback
client.connect(broker_address, port=port)          #connect to broker

client.loop_start()        #start the loop

while Connected != True:    #Wait for connection
    time.sleep(1)

try:
    while True:
        time.sleep(1)


except KeyboardInterrupt:
    print("exiting..")
    db.close()
    client.disconnect()
    client.loop_stop()
