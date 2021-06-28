import requests

URL = "https://api.adviceslip.com/advice"

def print_menu():
    print("(A)dvice    (Q)uit")

def get_command():
    return input("Enter a command: ").strip().lower()

def main():
    print_menu()
    command = get_command()

    while command != "q":
        if command != "a":
            print("Invalid command")
            print_menu()
            command = get_command()
            continue

        response = requests.get(URL)
        data = response.json()
        advice = data["slip"]["advice"]
        print(advice)

        print_menu()
        command = get_command()

main()