# How to UNPACK arguments
# Function that calculates the expected age you will live
def suspicious_calculator(age, fruit_ate, cigs_smoke):
    answer = (100 - age) + (fruit_ate * 3.5) - (cigs_smoke * 2)
    print(answer)


data_list = [27, 5, 0]

suspicious_calculator(data_list[0], data_list[1], data_list[2])
# for just one list of data its fine, but if want to do for lots of data (as arguments)
# it will take more lines of code, so a quick way will be using unpacking an arguments list,
# so will take the list and passes each item at the time:

suspicious_calculator(*data_list)

print()


# Using SETS: Collections of items which could have any duplicate items

groceries = {'cereal', 'milk', 'cereal', 'beer', 'lotion', 'beer'}
print(groceries)

# It prints all items but beer which has duplicate values only prints once

if 'milk' in groceries:
    print('You already have milk')
else:
    print('You need to add milk')

print()
# DICTIONARY: words with associated definitions, in python we call keys and values, For example
# classmates dictionary
classmates = {'Ryan': 'Cool chinese guy', 'Natalia': 'Cool english girl', 'Craig': 'Leam Neeson fan'}

print(classmates)
# Print only one value for a given key
print(classmates['Natalia'])

print()
# Looping through all keys
for k, v in classmates.items():
    print(k, ' ', v)


