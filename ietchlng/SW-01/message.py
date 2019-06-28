from twilio.rest import Client
import schedule
import time


def fun():
    a = 0
    f = open('file.txt', "r")
    t = round(time.time())
    account_sid = 'AC6016ffb984b8e96953a017215c27e782'
    auth_token = '57e13725780981a6a74621de25ad2c12'
    client = Client(account_sid, auth_token)
    for m in f:
        if(((int(m)-t) <= 15000)and(int(m)-t)>0):
            a = 1
            break

    if(a == 1):
        message = client.messages.create(
            to="+917761055179",
            from_="+12053509974",
            body="The contest is about to start. All the best!"
        )
        print(message.sid)

    else:
        print("Message will be sent when contest is near")


schedule.every().hour.do(fun)
while True:
    schedule.run_pending()
    time.sleep(2)
