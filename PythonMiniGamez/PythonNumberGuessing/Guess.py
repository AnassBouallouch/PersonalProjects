import random
import math


x = random.randint(1, 100)

guess = int(input("enter a number: "))

while x != guess:
    if guess < x:
        guess = int(input(" number too low try  again: "))
    elif guess > x:
        guess = int(input("number too high try again: "))

    else:
        break
print("you guessed it right!")





