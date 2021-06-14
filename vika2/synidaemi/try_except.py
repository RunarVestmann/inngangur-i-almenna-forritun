try:
    a_list = [1, 2, 3]
    print(a_list[90])
except IndexError:
    print("Index out of bounds")

print("Program ended")