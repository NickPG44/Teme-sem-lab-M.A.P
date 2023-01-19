import requests
import json

API_KEY = "e4d0bdbbf86411baca209d357bf017b4"
BASE_URL = "http://api.openweathermap.org/data/2.5/weather?q="
city = input('Introdu numele orasului:')
request_url = f"{BASE_URL}?appid={API_KEY}&q={city}"
rasp = requests.get(request_url)
data = json.loads(rasp.text)
print(data)