import relay_script
import pymysql
import csv
try:
    mySQLconnection = pymysql.connect(host='localhost',database='smartlab',user='pi',password='lunatics@92',unix_socket='/var/run/mysqld/mysqld.sock')
    sql_select_Query = "select * from sensor_values order by timestamp desc "
    cursor = mySQLconnection .cursor()
    cursor.execute(sql_select_Query)
    records = cursor.fetchone()
    print("Total number of rows in python_developers is - ", cursor.rowcount)
    print ("Printing each row's column values i.e.  developer record")
    print("timestamp = ", records[0])
    print("Soil_moisture = ",records[1])
    print("water level  = ", records[2])
    print("Nitrogen  = ", records[3])
    print("Phosphrous  = ", records[4])
    print("Potassium  = ", records[5])
    list=[]
    count=0
    rain=0
    row=[records[0],records[1],records[2],records[3],records[4],records[5]]
    c = csv.writer(open("/home/pi/Desktop/temp.csv","wb"))
    c.writerow(row)
    #
    #load the model and predict it and then send those values to be checked with the
    #current if they fall short advise with an if
    #
    sm_threshold=500
    sm_threshold=50
    f=open('/home/pi/parsed_weather_data.txt','r')
    str=f.read()
    list=str.split(":")
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
    cursor.close()
finally:
    #closing database connection.
    mySQLconnection.commit()
    print("MySQL connection is closed")


