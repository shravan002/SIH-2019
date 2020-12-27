import json

with open('weather.json') as json_file:
    data = json.load(json_file)
    count = 0
    flag = 0
    f = open('parsed_weather_data.txt','w')
    for p in data['list']:
        for q in p['weather']:
            if count < 16:
                count += 1  
                data = q['main']
                f.write(data + ',')    
                #print('Forecast: ' + q['main'])
                #print(' ')
            else : 
                flag = 1
                break
        if flag == 1 : 
            break


