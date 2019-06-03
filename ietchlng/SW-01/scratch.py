import requests
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
