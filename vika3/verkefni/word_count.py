filename = input("Enter filename: ")

try:
    file_object = open(filename)
    word_dict = dict()

    for line in file_object:
        for word in line.strip().split():
            if word in word_dict:
                word_dict[word] += 1
            else:
                word_dict[word] = 1

    print(word_dict)

    file_object.close()
except FileNotFoundError:
    print(f"{filename} was not found")