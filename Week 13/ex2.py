import requests
import time
import json
url = "http://api.open-notify.org/iss-now.json"
print("Connecting to ISS satellite...")
response = requests.get(url)
if response.status_code == 200:
    print("Connection Successful!")
    my_d = json.loads(response.text)
    latitude = my_d['iss_position']['latitude']
    longitude = my_d['iss_position']['longitude']
    print("Current Location:")
    print(f"Latitude: {latitude}")
    print(f"Longitude: {longitude}")