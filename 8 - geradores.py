import random

def get_numbers():
    while True:
        number = random.random()
        if number > 0.1:
            yield number
        else:
            break

def multiply(number):
    print('Multiplying number ' + str(number))
    return number * 2

def filter_(number):
    print('Filtering number ' + str(number))
    return number > 0.4

multiplied = map(multiply, get_numbers())
filtered = filter(filter_, multiplied)

print(list(filtered))