# Simple examples defining functions


def firstFunction():
    print('Functions are very cool!!')

firstFunction()


def convert_bitcoint_to_usd(btc):
    amount = btc * 435
    print(btc, ' is equivalent to: ', amount)

convert_bitcoint_to_usd(3.45)
convert_bitcoint_to_usd(4)

# Returning values from a function
# The function below returns the age of a girl (max of 7 years older) that can boy date


def calculate_dating_age(my_age):
    girls_age = my_age//2 + 7;
    return girls_age


my_age = 25
date_age = calculate_dating_age(my_age)
print('If you age is', my_age, 'you can date with girls', date_age, 'or older')


# Rather than doing for just a given age, we can do a table for different ages

print()
for i in range(15,60):
    current_age = calculate_dating_age(i)
    print('for boy age', i, 'can date girls',current_age,'or older')


# Default values for arguments
print()
def get_gender(sex='unknown'):
    if sex == 'M':
        sex = 'Male'
    elif sex == 'F':
        sex = 'Female'
    print(sex)

get_gender()
get_gender('M')
get_gender('F')

# Variables Scope

aux = 77


def func1():
    print(aux)


def func2():
    aux = 88
    print(aux)

func1()
func2()

# Keyword Arguments


def complex_function(name = 'Yo', surname = 'Soy', action = 'Sospechoso'):
    print(name, surname, action)

complex_function()

complex_function(action = 'Super hero', name = 'Yo no a')


print('-------------------')

numbers = [6, 7, 8, 9, 10]
total = 0
for j in numbers:
    print('number to add is', j)
    total = total + j

print('total is', total)

'''
list_of_lists = [ [1, 2, 3], [4, 5, 6], [7, 8, 9]]
for list in list_of_lists:
    print(list)
    for x in list:
        print(x)
'''

print()

# Function that receives any amount of arguments.


def any_arguments(*args):
    total_sum = 0
    total_sum1 = 0
    print('argument value = ', args)
    for i in args:
        print('value i =', i)
        total_sum = total_sum + i
        total_sum1 += i

    print('Total Sum =', total_sum)
    print('Total Sum2 =', total_sum1)

print('One argument')
any_arguments(4)
print()
print('Two arguments')
any_arguments(3, 4)
print()
print('More arguments')
any_arguments(8, 20, 44, 50)

