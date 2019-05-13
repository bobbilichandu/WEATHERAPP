from flask import Flask,render_template,request
import plivo
from data import weather

app=Flask(__name__)
def fun(destination,cityid):
    auth_id='MAMZNKMJJJYZJKNWQWNZ'
    auth_token='MzlkYmJiOGIxNDcwYzMxNWQyMTgzODkxMzE1YmEy'
    messagedic=weather(cityid)
    source='+91963498372'
    message=" "
    if messagedic['status']==10:
        message=message+"CITY ID IS INCORRECT"
        
    elif messagedic['status']==1:
        message = message+"NAME OF CITY IS: "+str(messagedic['name of city']) +", "
        message = message+"LONGITUTE:"+str(messagedic['lon'])+", "
        message = message+"LATITUDE:"+str(messagedic['lat'])+", "
        message = message+"WEATHER:"+str(messagedic['weather'])+", "
        message = message+"MAX TEMPERATURE"+str(messagedic['maximum_temperature'])+"F, "
        message = message+"MIN TEMPERATURE"+str(messagedic['minimum_temperature'])+"F"

    client = plivo.RestClient(auth_id=auth_id, auth_token=auth_token)
    messages=client.messages.create(src=source,
    dst=destination,
    text=message)
    print(messages)
@app.route('/send',methods=['GET','POST'])
def send():
    if request.method == "POST":
        destination=request.form['dst']
        message=request.form['msg']
        fun(destination,message)
        return render_template('success.html')
    return render_template('main.html')

if __name__=="__main__":
    app.run()