import requests
country = requests.get("http://ip-api.com/json").json().get("country")
print("Detected Country:", country)
