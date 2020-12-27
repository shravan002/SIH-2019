# -*- coding: utf-8 -*-
"""
Created on Sun Jul 21 17:44:50 2019

@author: Sameer Gupta
"""
from datetime import date
import numpy as np
import matplotlib.pyplot as plt
import pandas as pd
import pymysql
import motor_control
import send_notification as sms




def phosphorous_check (p) :
    date1=date(2019,7,16)#actual start date  of the crop
    date2=date.today()#current date
    day_count=abs(date2-date1).days
    list=[]
    df=pd.read_csv("phosphorous_data.csv",header=None)

    p=int(p)


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

    if(X_mean[day_count]>=2.9 and X_mean[day_count]<=3.3 ):
        if(p>=2.45 and p<=2.8):
            check_level=1  #1 means low
        elif( p<2.45):
            check_level=0    #0 very low

    elif (X_mean[day_count]>=3.4):
        if(p>=3.4):
            check_level=2
        elif(p<=2.45 and p>=2.8):
            check_level=0
        elif( p<=3.3 and p>=2.9):
            check_level=1

    elif (X_mean[day_count]>=2.45 and X_mean[day_count]<=2.8):
        if(p<2.45):
            check_level=1
        else:
            check_level=2
    sms.notification(check_level,"phosphorous")
    return X_mean[day_count]
