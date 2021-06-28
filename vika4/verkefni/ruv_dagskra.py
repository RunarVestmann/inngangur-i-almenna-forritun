import requests

URL = "https://apis.is/tv/ruv"

def main():
    response = requests.get(URL)
    data = response.json()["results"]

    file_object = open("ruv_dagskra.txt", "w", encoding="utf8")

    for show in data:
        print(f"{show['title']} {show['startTime']}")
        file_object.write(f"{show['title']} {show['startTime']}\n")
    file_object.close()

main()