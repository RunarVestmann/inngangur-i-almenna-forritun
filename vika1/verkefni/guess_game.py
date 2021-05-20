number = 10
guess = int(input("Guess a number: "))
if guess < number:
    print("Your guess is too small")
elif guess > number:
    print("Your guess is too large")
else:
    print("You guessed the correct number!")