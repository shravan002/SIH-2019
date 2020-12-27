# -*- coding: utf-8 -*-
"""
Created on Sun Jul 21 15:36:46 2019

@author: Sameer Gupta
"""
from datetime import date
import numpy as np
import matplotlib.pyplot as plt
import pandas as pd
import pymysql
import motor_control
import send_notification as sms


def potassium_check (k) :
    date1=date(2019,7,16)#actual start date  of the crop
    date2=date.today()#current date
    day_count=abs(date2-date1).days

    list=[]
    df=pd.read_csv("potassium_data.csv",header=None)

    k=int(k)


    r,c=df.shape
    #level from 1 to 6 where 1 stands for dry and going on to state 6 fully moist
    array_level = [[0]*c]*r

    list = [[]]*r

    list=df.values.tolist()
    X_min=np.amin(array_level,axis=0)
    X_max=np.amax(array_level,axis=0)
    X_mean=np.mean(array_level,axis=0)

    X_mid=[]
    for i in range(0,134) :
        X_mid.append((X_max[i]+X_min[i])/2)


    check_level=2   #2 means ok as reuired
    ###check for the level

    if(X_mean[day_count]>=2.3 and X_mean[day_count]<=2.8 ):
        if(k>=1.6 and k<=2.2):
            check_level=1  #1 means low
        elif( k<1.6):
            check_level=0    #0 very low

    elif (X_mean[day_count]>=2.9):
        if(k>=3.4):
            check_level=2
        elif(k<=2.3 and k>=2.8):
            check_level=1
        elif( k<=1.6 and k>=2.2):
            check_level=0

    elif (X_mean[day_count]>=1.6 and X_mean[day_count]<=2.2):
        if(k<1.6):
            check_level=1
        else:
            check_level=2
    print("done")
    sms.notification(check_level,"potassium")
    return X_mean[day_count]
