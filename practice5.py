import random

number = random.randint(1,20)
print('I am thinking of a number between 1 and 20. ')

for numOfTries in range(1,7):
    print('Take a guess. ')
    guess = int(input())

    if guess > number:
        print("Too high.")
    elif guess < number:
        print("Too low")
    else:
        break

if guess == number:
    print('Correct answer! in ' + str(numOfTries) + ' tries. ')
else:
    print("The number is " + str(number))



