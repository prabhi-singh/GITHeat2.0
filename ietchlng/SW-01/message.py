import nexmo
import schedule
import time


def fun():
    a = 0
    f = open('file1.txt', "r")
    t = round(time.time())
    for m in f:
        if(((int(m)-t)<=15000)and(int(m)-t)>0):
            a = 1
            break
    if (a == 1):
        client = nexmo.Client(key='c6e745b0', secret='............Rpme')
        client.send_message({
            'from': 'Nexmo',
            'to': '917761055179',
            'text': 'Contest is about to start. All the best. See you on the leader board.'
        })
    else:
        print("Contest is not near at the moment. Message will be sent when it is near.")


schedule.every().hour.do(fun)
while True:
    schedule.run_pending()
    time.sleep(2)
