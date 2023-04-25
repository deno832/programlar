import requests

url = 'http://192.168.1.5:800/is_exists/123123'
myobj = {"first_name": "deniz", "password":"seadsd"}

x = requests.get(url)

print(x.text)