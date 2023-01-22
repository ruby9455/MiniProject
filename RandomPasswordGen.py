
# Random Password Generator
import random
import string

# diffent lists of available combinations
upper = list(string.ascii_uppercase)
lower = list(string.ascii_lowercase)
nums = [str(i) for i in range(10)]
special = list(string.punctuation)

# selecting pw requirement
choices = [0, 1, 2, 3, 4]
availableChar = []

# ask for pw length
pwLen = input("Enter the password length: ")
# check if input is a digit
while not pwLen.isdigit():
    print("It's not a number")
    pwLen = input("Enter the password length: ")
pwLen = int(pwLen)
print()
while True:
    print("====================================================")
    print("== Select the requirement, separate them by space ==")
    print("====================================================")
    print("==                 1 uppercase                    ==")
    print("==                 2 lowercase                    ==")
    print("==                   3 number                     ==")
    print("==              4 special characters              ==")
    print("==                     0 quit                     ==")
    print("====================================================")
    requirement = list(map(int, input().split(" ")))
    for r in requirement:
        if r not in choices:
            print("Your selection is invalid")
            break
    break

# creating list of available char
if 0 in requirement:
    exit()
if 1 in requirement:
    availableChar += upper
if 2 in requirement:
    availableChar += lower
if 3 in requirement:
    availableChar += nums
if 4 in requirement:
    availableChar += special

print("".join(random.sample(availableChar, pwLen)))
