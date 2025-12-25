import requests
import json
api = "https://randomuser.me/api/?results=10&nat=us"
response = requests.get(url = api)
print("Fetching data from API...")
results = json.loads(response.text)['results']
s = 'first_name,last_name,email,city\n'
for i in results:
    f_n = i['name']['title']+'.'+i['name']['first']
    l_n = i['name']['last']
    email = i['email']
    city = i['location']['city']
    s += f"{f_n},{l_n},{email},{city}\n"
print("Successfully fetched 10 users.")
print("Writing to fake_users.csv...")

filename = 'fake_users.csv'
with open(filename, 'w') as f:
    f.write(s)
print("Done!")