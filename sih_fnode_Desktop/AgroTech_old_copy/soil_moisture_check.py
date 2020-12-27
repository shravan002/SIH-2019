from random import *
from datetime import date
import numpy as np
import pandas as pd
import pymysql

def soil_moisture_check (records) :
        date1=date(2019,7,16)#actual start date  of the crop
        date2=date.today()#current date
        day_count=abs(date2-date1).days
        
        #print("water_level_data  = ", records)
        list=[] 
        df=pd.read_csv("soil_moisture_data.csv",header=None)
        
       
        r,c=df.shape
        #level from 1 to 6 where 1 stands for dry and going on to state 6 fully moist
        array_level = [[0]*c]*r
        
        list = [[]]*r
        
        list=df.values.tolist()
        for i in range(0,r):
            for j in range(0,c):
                if list[i][j] <= 70 :
                    array_level[i][j]=6
                    
                elif (list[i][j] > 70 and list[i][j]<= 185) :
                    array_level[i][j]=5
                    
                elif (list[i][j] > 185 and list[i][j]<= 236):
                    array_level[i][j]=4
                
                elif (list[i][j] > 236 and list[i][j]<= 350):
                    array_level[i][j]=3
                
                elif (list[i][j] > 350 and list[i][j]<= 652):
                    array_level[i][j]=2
                
                else :
                    array_level[i][j]=1
                
                
                
        X_min=np.amin(array_level,axis=0) 
        X_max=np.amax(array_level,axis=0)
        X_mean=np.mean(array_level,axis=0)
        
        
        for i in range(day_count-1,day_count) :            
            if ( X_mean[i] >= records[1] ):
                upto_level=round((X_max[i]+X_mean[i])*0.75)
            else :
                upto_level=0
        
        return upto_level,array_level



