
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
            url = "https://www.fast2sms.com/dev/bulk"
            payload = payload +str +" is "+level+" \n " +"Please apply Urea."+"&language=english&route=p&numbers=9736538118"
            headers = {
        	'authorization': "ncQTauSVOr83F2ylHqoAbdDMjsU4Jp0mi9tCReY5LKzZE61vNwqMLUsTht9je3w1f82NiAO6HSDcdpvz",
        	'Content-Type': "application/x-www-form-urlencoded",
        	'Cache-Control': "no-cache",
                }
            response = requests.request("POST", url, data=payload, headers=headers)
            print("Message Send")
