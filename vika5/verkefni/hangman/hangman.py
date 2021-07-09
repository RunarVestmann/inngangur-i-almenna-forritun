import random

FILENAME = "words.txt"
GUESS_COUNT = 12

def get_file_object(filename):
    try:
        file_object = open(filename)
        return file_object
    except FileNotFoundError:
        return None

def get_word_list(file_object):
    word_list = []

    for word in file_object:
        word_list.append(word.strip().lower())
    
    return word_list

def get_random_word():
    file_object = get_file_object(FILENAME)

    if file_object == None:
        print("The file: {FILENAME} was not found")

    word_list = get_word_list(file_object)

    if len(word_list) == 0:
        print(f"There are no words in the file: {FILENAME}")
        return None

    word = word_list[random.randint(0, len(word_list)-1)]

    return word

def show_progress(word, user_guess_list):
    for letter in word:
        if letter in user_guess_list:
            print(letter, end=" ")
        else:
            print("_", end=" ")
    print()

def is_game_won(word, user_guess_list):
    for letter in word:
        if letter not in user_guess_list:
            return False
    return True

def prompt_user_to_guess(guesses_made, user_guess_list, word_to_guess):
    user_guess = input(f"Enter guess {guesses_made}/{GUESS_COUNT}: ").lower().strip()

    while user_guess in user_guess_list:
        print(f"You already guessed: {user_guess}")
        show_progress(word_to_guess, user_guess_list)
        user_guess = input(f"Enter guess {guesses_made}/{GUESS_COUNT}: ").lower().strip()
    
    return user_guess

def add_guess_to_guess_list(guess, guess_list, word_to_guess):
    if guess == word_to_guess:
        for letter in guess:
            guess_list.append(letter)
    else:
        guess_list.append(guess)

def main():
    user_wants_to_play = True
    while user_wants_to_play:
        word_to_guess = get_random_word()

        if word_to_guess == None:
            break

        user_guess_list = []

        for i in range(GUESS_COUNT):
            show_progress(word_to_guess, user_guess_list)

            if is_game_won(word_to_guess, user_guess_list):
                print("Congratulations you won!")
                break

            user_guess = prompt_user_to_guess(i+1, user_guess_list, word_to_guess)

            add_guess_to_guess_list(user_guess, user_guess_list, word_to_guess)
        
        print(f"The word was {word_to_guess}")

        user_input = input("Want to play again? (y/n): ").lower().strip()
        user_wants_to_play = user_input.startswith("y")

main()