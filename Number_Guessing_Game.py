# Write a program that asks the user to guess a number and tells whether the guess is correct, too high, or too low.

import random

secret_number = random.randint(-1000, 1000)
guess_num = int(input("Guess a secret number: "))

if guess_num > secret_number:
    print("Too high!")
elif guess_num < secret_number:
    print("Too low!")
else:
    print("Guess is correct!")

print("The secret number was: " , secret_number)
