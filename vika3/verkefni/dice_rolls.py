import random

number = int(input("Enter how many times: "))

dice_dict = {}

for i in range(number):
    roll = random.randint(1, 6)
    if roll in dice_dict:
        dice_dict[roll] += 1
    else:
        dice_dict[roll] = 1
    
for key in dice_dict:
    print(f"{key} came up {dice_dict[key]} times")