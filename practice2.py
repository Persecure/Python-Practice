
passwordFile = open('secret.txt') # password file is secret.txt *create a secret.txt file with password inside in the code folder*
secretPassword = passwordFile.read() # The password is in the contents of secret.txt
print('Enter your password ')
typedPassword = input()             # User Input
if typedPassword == secretPassword:
    print('Acess granted')
else:
    print('Access Denied')
