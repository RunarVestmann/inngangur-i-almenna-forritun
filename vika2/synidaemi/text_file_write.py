file_object = open("test_write.txt", "w")
name_list = ["Bob", "Eve", "John"]

for name in name_list:
    file_object.write(name + "\n")

file_object.close()