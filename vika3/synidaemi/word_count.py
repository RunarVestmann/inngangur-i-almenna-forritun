import string

filename = input("Enter filename: ")

try:
    file_object = open(filename)
    word_dict = dict()

    # Fill the word dictionary
    for line in file_object:
        for word in line.strip().split():
            word = word.strip(string.punctuation)
            for word in word.split("-"):
                word = word.lower()
                if word == "":
                    continue
                if word in word_dict:
                    word_dict[word] += 1
                else:
                    word_dict[word] = 1

    # Sort the words in the descending count order
    word_list = list(word_dict.items())
    word_list.sort(key=lambda word_tuple: word_tuple[1], reverse=True)

    # Print the 20 most popular words
    for word, count in word_list[:20]:
        print(f"'{word}' came up {count} times")

    file_object.close()
except FileNotFoundError:
    print(f"{filename} was not found")