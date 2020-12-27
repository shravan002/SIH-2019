from random import *
from datetime import date
import numpy as np
import pandas as pd
import pymysql

def soil_moisture_check (sm) :
        date1=date(2019,7,16)#actual start date  of the crop
        date2=date.today()#current date
        day_count=abs(date2-date1).days
        
        #print("water_level_data  = ", records)
        df=pd.read_csv("new_soil_moisture_data.csv",header=None)
        
        
        r,c=df.shape
        #level from 1 to 5 where 
        #1 stands for dry and going on to state 5 fully moist
                
        list = [[]]*r
        
        list=df.values.tolist()
        
        array_level=level_to_cm_unit(list,r,c)
        sm_list=[[sm]]
        sm_level=level_to_cm_unit(sm_list,1,1)           
                
        X_min=np.amin(array_level,axis=0) 
        X_max=np.amax(array_level,axis=0)
        X_mean=np.mean(array_level,axis=0)
        #print(sm)
        #print(X_mean[day_count])
        #print(day_count)
        if ( X_mean[day_count] <sm ):
            upto_level=int((X_max[day_count]+X_mean[day_count])/2)
        else :
            upto_level=0
            
        if upto_level == 5 :
             upto_sm=250
                    
        elif upto_level == 4 :
             upto_sm=250
                    
        elif upto_level == 3 :
             upto_sm=250
                
        elif upto_level == 2 :
             upto_sm=250
     
        else :
             upto_sm=250  
        
        return upto_sm,sm_level,X_mean[day_count]

def level_to_cm_unit(list,r,c):
    array_level = [[0]*c]*r
    for i in range(0,r):
            for j in range(0,c):
                if list[i][j] <= 250 :
                    array_level[i][j]=5
                    
                elif (list[i][j] > 250 and list[i][j]<= 340) :
                    array_level[i][j]=4
                    
                elif (list[i][j] > 340 and list[i][j]<= 630):
                    array_level[i][j]=3
                
                elif (list[i][j] > 630 and list[i][j]<= 795):
                    array_level[i][j]=2
                else :
                    array_level[i][j]=1
                
    return array_level     

#x=soil_moisture_check(200)
#sm=200
