def weather(id):
    import json,requests
    url = "http://api.openweathermap.org/data/2.5/weather?id="+str(id)+"&APPID=a2c65944743eb5493d8970a7ee7d1023"
    r=requests.get(url)
    data=r.json()
    # print(data)
    dic={}
    if data['cod']==400 or data['cod']==404:
        dic['status']=10
        print(dic)
        return dic
    elif data['cod']==200:
        dic['status']=1
        coordinates=data['coord']
        for a in data['coord']:
            dic[a]=coordinates[a]
            # print(str(a)+ ":   " +str(coordinates[a]))
        weth=data['weather']
        weth1=weth[0]
        # print(weth1['main'])
        dic['weather']=str(weth1['main'])+" - "+str(weth1['description'])
        sys=data['main']
        dic['maximum_temperature']=sys['temp_max']
        dic['minimum_temperature']=sys['temp_min']
        dic['name of city']=data['name']
        print(dic)
        return dic
    


