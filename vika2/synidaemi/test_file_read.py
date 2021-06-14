file_object = open("test_write.txt")

name_list = []

for line in file_object:
    name_list.append(line.strip())

print(name_list)

file_object.close()