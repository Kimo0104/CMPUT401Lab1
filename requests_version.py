import requests

print(requests.get("http://www.google.com"))
print(requests.get("https://raw.githubusercontent.com/Kimo0104/CMPUT401Lab1/master/requests_version.py").text)