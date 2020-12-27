#*- coding: utf-8 -*-
"""
Created on Thu Jul 18 17:43:17 2019

@author: Sameer Gupta
"""
from random import *
from datetime import date
import numpy as np
import pandas as pd
import pymysql

def water_level_check (records) :
        date1=date(2019,7,16)#actual start date  of the crop
        date2=date.today()#current date
        day_count=abs(date2-date1).days

        #print("water_level_data  = ", records)
        list=[] 
        df=pd.read_csv("water_level_data.csv",header=None)

        r,c=df.shape

        array_cm = [[0]*c]*r

        list = [[]]*r

        list=df.values.tolist()
        for i in range(0,r):
            for j in range(0,c):
                if list[i][j] <= 13 :
                    array_cm[i][j]=0.2

                elif (list[i][j] > 13 and list[i][j]<= 43) :
                    array_cm[i][j]=0.5

                elif (list[i][j] > 44 and list[i][j]<= 65):
                    array_cm[i][j]=0.5+(list[i][j]/65)

                elif (list[i][j] > 66 and list[i][j]<= 113):
                    array_cm[i][j]=1.0+(list[i][j]/113)

                elif (list[i][j] > 114 and list[i][j]<= 143):
                    array_cm[i][j]=1.5+(list[i][j]/143)

                elif (list[i][j] > 144 and list[i][j]<= 157):
                    array_cm[i][j]=2.0+(list[i][j]/157)

                elif (list[i][j] > 157 and list[i][j]<= 158):
                     array_cm[i][j]=2.5+(list[i][j]/157)

                elif (list[i][j] > 158 and list[i][j]< 162):
                     array_cm[i][j]=3.5+(1.2*(list[i][j]/162))

                else :
                     a=(randint(33,150)/100)
                     array_cm[i][j]=4+a

        X_min=np.amin(array_cm,axis=0) 
        X_max=np.amax(array_cm,axis=0)
        X_mean=np.mean(array_cm,axis=0)

        X_mid=[]
        for i in range(0,134) :
            X_mid.append((X_max[i]+X_min[i])/2)



        for i in range(day_count-1,day_count) :
            if ( X_mean[i] >= X_mid[i] ) :
                if ( X_mean[i] >= records[1] ):
                    upto_level=X_max[i]
                else :
                    upto_level=0;
            elif ( X_mean[i] < mid[i] ) :
                if ( X_mean[i] >= records[1] ):
                    upto_level=(X_mid[i]+X_max[i])/2
                else :
                    upto_level=0

        upto_level=(round(upto_level/0.5))*0.5
        return upto_level,array_cm



