import random

number = random.randint(1, 100)
guess = int(input("Guess a number between 1-100: "))
while guess != number:
    if guess < number:
        print("Your guess is too small")
    else:
        print("Your guess is too large")
    guess = int(input("Guess a number between 1-100: "))

print("You guessed the correct number!")