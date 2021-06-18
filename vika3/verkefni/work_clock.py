from datetime import datetime

def print_menu():
    print("(C)lock    (G)et status    (Q)uit")

def clock(name, name_dict):
    if name in name_dict:
        name_dict[name].append(datetime.now())
    else:
        name_dict[name] = [datetime.now()]

def print_status(name, name_dict):
    lowercase_name = name.lower()
    if lowercase_name in name_dict:
        is_clocked_in = len(name_dict[lowercase_name]) % 2 != 0
        if is_clocked_in:
            print(f"{name} is clocked in and has been working since {name_dict[lowercase_name][-1].strftime('%d/%m/%Y %H:%M')}")
        else:
            print(f"{name} is clocked out and has been off duty since {name_dict[lowercase_name][-1].strftime('%d/%m/%Y %H:%M')}")
    else:
        print(f"{name} has never used the clock")

def main():
    name_dict = dict()

    print_menu()
    command = input("Enter a command: ").strip().lower()
    while command != "q":
        name = input("Enter a name: ").strip()

        if command == "c":
            clock(name.lower(), name_dict)
        else:
            print_status(name, name_dict)

        print_menu()
        command = input("Enter a command: ").strip().lower()

main()