
person_names = []

while True:
    print('Enter the name of the person ' + str(len(person_names)+1) + ' : Enter nothing to stop')
    names = input()
    if names == "":
        break
    person_names = person_names + [names]
print("The list of names are: ")
for name in person_names:
    print(name)

