age = 21
name = 'lucass'

print('Example if statement')

if age < 21:
    print('No beer for you')
elif age >= 21:
    print('You allow to drink beer')

if name is 'chris':
    print('Name is Chris')
elif name is 'lucas':
    print('Name is lucas')
elif name is 'craig':
    print('Name is craig')
else:
    print('No name is printed')

print()
print('-----------------')
print('Example using for loop and loop through a list of elements')

forloop = ['one','two','three','four','five','six','seven','eight','nine','ten']

for i in forloop:
    print(i + ' - length of string --> ' + str(len(i)))
#   print(i, ' - length of string --> ', len(i))

print()
print('-----------------')
print('Example using range function')

for j in range(6,16,2):
    print(j)

print()
print('-----------------')
print('Example using while loop')

while age < 10:
    print(age + ' is greater than 10')


print()
print('-----------------')
print('Example looping through a list and check if number given is in the list ')

magic_number = 14

for x in range(20):
    if x is magic_number:
        print(x, ' -- is the magic number')
        break
    else:
        print(x)


print()
print('-----------------')
print('Example looping through a list number (50) and print numbers that are multiple of 4')

for x in range(1,50):
    if x % 4 == 0:
        print(x, ' --> multiple of 4')

print()
print('-----------------')
print('Example Continue command, example checks if number have been taken from the list, if yes do not print')

numbersTaken = [3, 7, 15, 8, 23]
print('Here are the number that still available')

for y in range(30):
    if y in numbersTaken:
        continue
    print(y)

print('End examples')
