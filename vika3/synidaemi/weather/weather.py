import requests

URL = "https://apis.is/weather/forecasts/is?stations="

def print_menu():
    print("(G)et data    (Q)uit")

def get_command():
    return input("Enter a command: ").strip().lower()

def main():
    print_menu()
    command = get_command()
    while command != "q":

        if command != "g":
            print("Invalid command")
            print_menu()
            command = get_command()
            continue

        stations = input("Enter station numbers(seperated by a comma): ").strip().replace(" ", "")

        response = requests.get(URL + stations)
        if response.status_code == 404:
            print("Invalid input, station numbers could not be found")
            print_menu()
            command = get_command()
            continue

        data = response.json()["results"]

        for station in data:
            print(f"{station['name']}:")
            for info in station["forecast"]:
                print(f"\t{info['ftime']} Hiti:{info['T']}°C Lýsing:{info['W']}")

        print_menu()
        command = get_command()

main()
