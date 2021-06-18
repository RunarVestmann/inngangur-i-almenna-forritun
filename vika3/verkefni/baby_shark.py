def sing(word):
    for _ in range(3):
        print(f"{word}, doo, doo, doo, doo, doo, doo")
    print(word)
word_tuple = ("Baby shark", "Mommy shark", "Daddy shark", "Grandpa shark", "Let's go hunt", "Run away", "Safe at last", "It's the end")
for word in word_tuple:
    sing(word)