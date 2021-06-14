# List
name_list = ["Bob", "Eve", "John"]

name_list.append("Joe")
name_list.remove("Eve")

name_list[0] = "Arnar"

if "Arnar" in name_list:
    print("He's in the list")

for i in range(0, len(name_list)):
    print(name_list[i])

for name in name_list:
    print(name)

# Tuple (Immutable List)
name_tuple = ("Bob", "Eve", "John")

for i in range(0, len(name_tuple)):
    print(name_tuple[i])

for name in name_tuple:
    print(name)

# Set
name_set = {"Bob", "Eve", "John"}

name_set.add("Bob")

if "Eve" in name_set:
    name_set.remove("Eve")

for name in name_set:
    print(name)