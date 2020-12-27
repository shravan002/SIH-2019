
import pymysql
import os
import requests


def notification(check_level,str):
        payload="sender_id=FSTSMS&message=GreenSol"+ "\n" +"ATTENTION!" + "\n"
        
        if(check_level!=2):   
            
            if(check_level == 1 ):
                level="low"
            else:
                level="very low"
            
            tt=" is "
            
            check_level=int(check_level)
            if(str=="nitrogen"):
                fertilizer="Please apply Urea."
            elif( str=="potassium"):
                fertilizer="Please apply  Potassium Sulphate for  ."+str+" "
            elif(str=="phosphorous"):
                fertilizer="Please apply DAP for  ."+str+" "
            else:
                fertilizer=""
                level=""
                tt=""
                
                
            url = "https://www.fast2sms.com/dev/bulk"
            payload = payload +str +tt+level+" \n " +fertilizer+"&language=english&route=p&numbers=9736538118"
            headers = {
        	'authorization': "ncQTauSVOr83F2ylHqoAbdDMjsU4Jp0mi9tCReY5LKzZE61vNwqMLUsTht9je3w1f82NiAO6HSDcdpvz",
        	'Content-Type': "application/x-www-form-urlencoded",
        	'Cache-Control': "no-cache",
                }
            response = requests.request("POST", url, data=payload, headers=headers,verify=False)
            print(response)
            print("Message Send")


#notification(1,"test")
