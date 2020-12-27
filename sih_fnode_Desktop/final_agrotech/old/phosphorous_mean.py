# -*- coding: utf-8 -*-
"""
Created on Sun Jul 21 17:44:50 2019

@author: Sameer Gupta
"""

# -*- coding: utf-8 -*-
"""
Created on Wed Jul 17 23:35:48 2019

@author: Sameer Gupta
"""
# -*- coding: utf-8 -*-
"""
Created on Thu Jul 18 17:43:17 2019

@author: Sameer Gupta
"""


import numpy as np
import matplotlib.pyplot as plt
import pandas as pd
import pymysql
import realy_script
#defined



def potassium_check (k) :
    mySQLconnection = pymysql.connect(host='localhost',database='smartlab',user='pi',password='lunatics@92',unix_socket='/var/run/mysqld/mysqld.sock')
    sql_select_Query = "select * from sensor_values order by timestamp desc "
    cursor = mySQLconnection .cursor()
    cursor.execute(sql_select_Query)
    records = cursor.fetchmany(10)
    mySQLconnection.commit()
    cursor.close()
    mySQLconnection.close()
       
    print("Potassium  = ", records)
    list=[] 
    df=pd.read_csv("potassium.csv",header=None)
    X_min=df.min(axis = 1) 
    X_avg=df.mean(axis = 1)
    Y=np.arange(1, 135).tolist()
    X_var=[]
    X_max=df.max(axis = 1)
    for i in range(0,100) :
       X_var.append((X_max[i]-X_min[i])/3)
    for i in range(0,100) :
       m=(X_max[i]+X_min[i])/2
       X_max[i]=m+X_var[i]
       X_min[i]=m-X_var[i]
    for i in records:
            if i[5] !< X_min[] :
                #"to be done the day number maintaining a count"]) or (i[5] > X_max["to be done the day number maintaining a count"]) :
                #"run the relay script that  you have destroyed until the level is restored"
       


def display_graph():
    plt.plot(Y,X_min, color = 'red')
    plt.plot(Y,X_max, color = 'blue')
    plt.plot(Y,X_avg, color = 'black')
    plt.title('potassium in soil with days')
    plt.xlabel('no of days')
    plt.ylabel('nitrogen level')
    plt.show()
    


