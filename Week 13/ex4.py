import requests
import json
url = "http://universities.hipolabs.com/search"
country = input("Enter country name: ")
params = {'country': country}
response = requests.get(url=url, params=params)
my_l = json.loads(response.text)
if len(my_l) == 0: print(f"No universities found for {country}.")
else:
    print(f"Found 23 universities in {country}.")
    print(f"Here are the first 5:")
    for i in range(5):
        my_d = my_l[i]
        print(f"{i+1}. {my_d['name']}")