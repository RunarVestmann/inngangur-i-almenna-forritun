import requests

r = requests.get("https://apis.is/petrol")

data = r.json()

for station in data["results"]:
    if "Akureyri" in station["name"]:
        print(f"{station['company']} {station['name']} Bensínverð:{station['bensin95']}kr Dieselverð:{station['diesel']}kr")