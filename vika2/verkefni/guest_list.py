guest_set = set()

file_object = open("guest_list.txt", encoding="utf8")
for line in file_object:
    guest_set.add(line.strip().lower())
file_object.close()

print("(A)dd     (R)emove    (C)heck list    (S)earch list    (Q)uit")
choice = input("Enter your choice: ").lower().strip()

while choice != "q":
    if choice == "a":
        name = input("Enter a name: ").strip().lower()
        guest_set.add(name)
        file_object = open("guest_list.txt", "w", encoding="utf8")
        for name in guest_set:
            file_object.write(f"{name}\n")
        file_object.close()
    elif choice == "r":
        name = input("Enter a name to remove: ").strip().lower()
        if name in guest_set:
            guest_set.remove(name)
            file_object = open("guest_list.txt", "w", encoding="utf8")
            for name in guest_set:
                file_object.write(f"{name}\n")
            file_object.close()
    elif choice == "c":
        name = input("Enter a name to check: ").strip()
        if name.lower() in guest_set:
            print(f"{name} is on the guest list")
        else:
            print(f"{name} is not on the guest list")
    elif choice == "s":
        search = input("Enter a name to search for: ").strip().lower()
        for name in guest_set:
            if search in name:
                print(name)
    print("(A)dd     (R)emove    (C)heck list    (S)earch list    (Q)uit")
    choice = input("Enter your choice: ").lower().strip()
