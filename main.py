# This is a sample Python script.

# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.


import random

guessesTaken = 0

print("Hello! What is your name? ")
#function input will take in user string and assignment to variable myName
myName = input()
#library random is used, specified random integer, instead of float or other
number = random.randint(1,20)
print("well " + myName + " I am thinking of a number between 1 and 20")

#range is a function counting from 0-5
for guessesTaken in range(6):
    print("take a guess")
    guess = input()
    #input takes in user input as string so must cast to int
    guess = int(guess)

    if guess < number:
        print("your guess is too low.")
    if guess > number:
        print("your guess is too high")
    if guess == number:
        break

if guess == number:
    guessesTaken = str(guessesTaken + 1)
    print("good job " + myName + " you guessed my number in " + guessesTaken + " guesses")

if guess != number:
    number = str(number)
    print("nope, the number i was think of was" + number + ".")

