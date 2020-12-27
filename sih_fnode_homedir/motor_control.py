import time
import datetime
import pymysql

db = pymysql.connect(db="smartlab", user="pi", passwd="lunatics@92",unix_socket="/var/run/mysqld/mysqld.sock")

with db:
    cur = db.cursor()
    cur.execute("select * from sensor_values order by timestamp desc limit 1")
    rows = cur.fetchall()

    for row in rows:    
        if(
        
        