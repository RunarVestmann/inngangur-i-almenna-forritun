file_object = open('test.txt')

for line in file_object:
    print(line.strip())

file_object.close()