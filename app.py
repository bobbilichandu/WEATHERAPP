from flask import Flask,render_template,request
import plivo
from a import wdata

app=Flask(__name__)

def fun(destination):
    auth_id='your auth id'
    auth_token='your auth token'
    source='YOUR SOURCE PHONE NUMBER'
    message=" "
    
    messagedic = wdata(1)
    count=0
    for key in messagedic:
        count = count + 1
        message = message + str(key) + ":  " + str(messagedic[key] ) + ","
        if count >10:
            break
    client = plivo.RestClient(auth_id=auth_id, auth_token=auth_token)
    messages=client.messages.create(src=source,
    dst=destination,
    text=message)
    print(messages)
@app.route('/send',methods=['GET','POST'])
def send():
    if request.method == "POST":
        destination=request.form['dst']
        fun(destination)
        return render_template('success.html')
    return render_template('main.html')

if __name__=="__main__":
    app.run()