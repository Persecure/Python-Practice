def collatz(number):

    if number % 2 == 0:
        print(number // 2)
        return number // 2
    elif number % 2 == 1:
        result = (number * 3 + 1)
        print(result)
        return result

number = input('Enter a number ')

while number != 1:
    number = collatz(int(number))
