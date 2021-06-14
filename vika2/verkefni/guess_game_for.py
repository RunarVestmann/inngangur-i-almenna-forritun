import random

number = random.randint(1, 100)
for i in range(0, 5):
    guess = int(input("Guess a number between 1-100: "))
    if guess < number:
        print("Your guess is too small")
    elif guess > number:
        print("Your guess is too large")
    else:
        print("You guessed the correct number!")
        break

