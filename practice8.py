
people = ['john','tom','sally','bob','mike']

for i in range(len(people)):
    print('Index ' + str(i) + ' is ' + people[i] )

print('cat' in people)                                    # Check if an item is in the list
print(people.index('tom'))                                # Use the index method to indicate location of item in the list
