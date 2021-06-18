import string

def open_file(filename):
    try:
        file_object = open(filename)
        return file_object
    except FileNotFoundError:
        return None

def fill_dict(file_object):
    word_dict = dict()
    for line in file_object:
        for word in line.strip().split():
            word = word.strip(string.punctuation)
            for word in word.split("-"):
                word = word.lower()
                if word == '':
                    continue
                if word in word_dict:
                    word_dict[word] += 1
                else:
                    word_dict[word] = 1
    return word_dict

def get_sorted_word_list(word_dict, descending):
    word_list = list(word_dict.items())
    word_list.sort(key=lambda word_tuple: word_tuple[1], reverse=descending)
    return word_list

def print_result(word_list, total):
    for word, count in word_list[:total]:
        print(f"'{word}' came up {count} times")

def main():
    filename = input("Enter filename: ")
    file_object = open_file(filename)
    if file_object == None:
        return
    word_dict = fill_dict(file_object)
    file_object.close()
    word_list = get_sorted_word_list(word_dict, True)
    print_result(word_list, 20)

main()