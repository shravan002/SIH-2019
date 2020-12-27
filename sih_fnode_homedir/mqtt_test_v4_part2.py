import paho.mqtt.client as mqttClient
import time
import datetime
import pymysql

def on_connect(client, userdata, flags, rc):
    if rc == 0:
        print("Connected to broker test1")
        global Connected                #Use global variable
        Connected = True                #Signal connection
        #client.subscribe([("esp8266",2),("waterlevel",1)])
        client.subscribe("esp8266")
        print("Client Subscribed test2")
        print(Connected)
        time.sleep(10)
    else:
        print("Connection failed")

def on_message(client, userdata, message):
    print("Inside on_message function")
    print("Message received: "  + str(message.payload.decode("utf-8")))
    #print("******Message Topic: "+message.topic)
    #if (message.topic=="esp8266"): param="sm"
    #elif (message.topic=="waterlevel"): param="wl"

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

Connected = False   		#global variable for the state of the connection

broker_address= "192.168.0.5"   #Broker address
port = 1883                     #Broker port
user = "pi"                     #Connection username
password = "lunatics@92"        #Connection password


db = pymysql.connect(db="smartlab", user="pi", passwd="lunatics@92",unix_socket="/var/run/mysqld/mysqld.sock")

cursor = db.cursor()

client = mqttClient.Client(client_id="Python",clean_session=False)               #create new instance
client.username_pw_set(user, password=password)    #set username and password
client.on_connect= on_connect                      #attach function to callback
client.on_message= on_message                      #attach function to callback
client.connect(broker_address, port=port)          #connect to broker

client.loop_start()        #start the loop

while Connected != True:    #Wait for connection
    time.sleep(1)
    print("msg from while loop")

#client.subscribe([("esp8266",2),("waterlevel",1)])
#client.subscribe("esp8266")
#client.loop_start()
#client.subscribe("waterlevel")
#client.loop_start()

try:
    while True:
        time.sleep(1)


except KeyboardInterrupt:
    print("exiting..")
    db.close()
    client.disconnect()
    client.loop_stop()
