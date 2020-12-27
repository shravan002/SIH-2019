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

def water_level_check (wl) :
        date1=date(2019,7,16)#actual start date  of the crop
        date2=date.today()#current date
        day_count=abs(date2-date1).days
        
        
        #print("water_level_data  = ", records)
        df=pd.read_csv("new_water_level_data.csv",header=None)

        r,c=df.shape

        array_cm = [[0]*c]*r

        list_1 = [[]]*r

        ##maximum depth considered is 4 cmconsidering the size of our sensor and proof of concept of the idea
        list_1=df.values.tolist()
        wl_list=[[wl]]
        array_cm=level_to_cm_unit(list_1,r,c)
        wl_cm=level_to_cm_unit(wl_list,1,1)
        #print(wl_cm)
        print("\n%dth Day from sowing\n"%(day_count))

        X_min=np.amin(array_cm,axis=0) 
        X_max=np.amax(array_cm,axis=0)
        X_mean=np.mean(array_cm,axis=0)
        
        X_mean[day_count]=X_mean[day_count]
        X_mid=[]
        for i in range(0,134) :
            X_mid.append((X_max[i]+X_min[i])/2)
        
        
        if ( X_mean[day_count] > X_mid[day_count] ) :
            if ( X_mean[day_count] >= wl_cm[0][0] ):
                upto_level=((X_max[day_count]+X_mean[day_count])/2)
            else :
                upto_level=0;
        else :
            if ( X_mean[day_count] >= wl_cm[0][0] ):
                upto_level=(X_mid[day_count]+X_max[day_count]+X_mean[day_count])/3
            else :
                upto_level=0    
        
        upto_level=round((upto_level)/0.5)*0.5
        
        if(upto_level!=0):        
            if(upto_level==3.5 and upto_level>wl_cm[0][0]):
                upto_level=516-35
            elif(upto_level==3.0 and upto_level>wl_cm[0][0]):
                upto_level=498-35
            elif(upto_level==2.5 and upto_level>wl_cm[0][0]):
                upto_level=485-35
            elif(upto_level==2.0 and upto_level>wl_cm[0][0]):
                upto_level=455-35
            elif(upto_level==1.5 and upto_level>wl_cm[0][0]):
                upto_level=420-35
            elif(upto_level==1.0 and upto_level>wl_cm[0][0]):
                upto_level=365-35
            elif(upto_level==0.5 and upto_level>wl_cm[0][0]):
                upto_level=321-35
            else:
                upto_level=530-35
        if(upto_level==0):
            upto_level=wl-10
        
        return upto_level,array_cm
    
    
    
def level_to_cm_unit(list_1,r,c):
    array_cm = [[0]*c]*r
    l=list(list_1)
    
    for i in range(0,r):
        for j in range(0,c):
            if l[i][j] <= 116 :
                array_cm[i][j]+=0.2
            elif (l[i][j] > 116 and l[i][j]<= 321) :
                array_cm[i][j]=round(0.2+(l[i][j]-116)/(321-116),2)
            elif (l[i][j] > 321 and l[i][j]<= 370):
                array_cm[i][j]=round(0.5+0.5*((l[i][j]-321)/(370-321)),2)
            elif (l[i][j] > 370 and l[i][j]<= 420):
                array_cm[i][j]=round(1.0+0.5*((l[i][j]-370)/(420-370)),2)
            elif (l[i][j] > 420 and l[i][j]<= 455):
                array_cm[i][j]=round(1.5+0.5*((l[i][j]-420)/(455-420)),2)
            elif (l[i][j] > 455 and l[i][j]<= 485):
                z=2.0+0.5*((l[i][j]-455)/(485-455))
                array_cm[i][j]=round(z,2)
                #print(array_cm[i][j])
                #print(i,j)
                #print()
            elif (l[i][j] > 485 and l[i][j]<= 498):
                z=2.5+0.5*((l[i][j]-485)/(498-485))
                array_cm[i][j]=round(z,2)
                #print(array_cm[i][j])
                #print(i,j)
                #print()
            elif (l[i][j] > 498 and l[i][j]<= 516):
                z=3.0+0.5*((l[i][j]-498)/(516-498))
                array_cm[i][j]=round(z,2)
                #print(array_cm[i][j])
               # print(i,j)
               # print()
            else :
                array_cm[i][j]=4.0
   # print(array_cm[0][0])
    return array_cm

#x=water_level_check(300)

#wl=300
