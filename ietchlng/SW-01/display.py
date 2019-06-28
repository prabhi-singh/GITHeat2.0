import requests
import time
s = input("Enter the UserID\r\n")
response = requests.get('http://codeforces.com/api/user.info?handles='+s)
j = response.json()
k = j["result"]
l = k[0]
print("Username : "+l['firstName']+" "+l['lastName'])
print("Current rating : "+str(l['rating']))
print("Rank : "+l['rank'])
print("Country : "+l['country'])
print("Maximum rating :"+str(l['maxRating']))
print("Maximum rank : "+l['maxRank'])
f = open('file.txt', 'w')
res = input("To get the list of upcoming contests type y else n\r\n")
if(res == 'y'):
    ipt = input("Need a reminder press y else n\r\n")
    response1 = requests.get('http://codeforces.com/api/contest.list?gym=false')
    z = response1.json()
    x = z['result']
    for i in range(len(x)):
        y = x[i]
        if(y['phase'] == 'BEFORE'):
            print(y['name'], " Contest will start in", int((y['relativeTimeSeconds'])/(60*60*24*-1)), "days")
            if(ipt == 'y'):
                print(y['startTimeSeconds'], file=f)
time.sleep(2)


