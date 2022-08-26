import sys

while True:
    print('Please type something ')
    response = input()
    if response == 'exit':
        sys.exit()
    print('You typed '+ response + '.')
