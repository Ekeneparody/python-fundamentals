#Functions
#Types of functions
#-Functions that perform a task

def greet(first_name, last_name):
    print(f'Hi there {first_name} {last_name}')
    print('Welcome aboard')

greet("Ekene", "Amadi")
greet("Udoka", "Amadi")

#-Function that return a value

def get_greeting(name):
    return f"Hi {name}"

message = get_greeting('Udoka')
print(message)

#Keyword Arguements
def increment(number, by):
    return number + by

result = increment(2, 1)
print(result)

##*args
def multiply(*numbers):
    total = 1
    print(numbers)
    for i in numbers:
        print(i)

multiply(2, 3, 4, 5)
##

#**args
def save_user(**user):
    print(user['name'])

save_user(id = 1, name = "John", age = 20)


#scope
'''def greet():
    message = 'a'''


def fizz_buzz(input):
    if(input % 3 == 0) and (input % 5 == 0):
        return "FizzBuzz"
    if input % 3 == 0:
        return 'Fizz'
    if input % 5 == 0:
        return 'Buzz'
    if(input % 3 == 0) and (input % 5 == 0):
        return "FizzBuzz"
    return input


print(fizz_buzz(7))


def calculate(int1, int2):
    return int1 * int2


calculation = calculate(5, 10)
print(calculation)
