#Fundamentals in programming
print('Hello World')
#printing


course = 'Data Science'
num = 2
num_variable = 4.5
boolean  = True
#Variables


print(len(course))
print(course)
print(course.upper())
print(course.lower())
print(course[-1])
print(course[0:2])
#Strings

#\"
#\'
#\\
#\n
#Escape sequences


first = 'Mosh'
last = 'Pablo'

full = first + " " + last
print(full)

#or

full = f"{first} {last}"
print(full)
#Concatenation



course = '   Data Science'
print(course.strip())
print(course.find('Sci'))
print("Dat" in course)
#String methods

import math
print(round(2.9))
print(abs(-2.9))

#num and math module



'''x = input("x: ")
y = int(x) + 1
print(f"x is {x} and y is {y}")'''

#Asking the user for input
#type conversion
#N.B=> python receives user input as string






#EXCERCISE1
#Write a program that uses input to prompt a user for their name and then welcomes them.
'''name = input("Enter your name:\n ")
print(f"Welcome {name.capitalize()}")


#Excercise 2
Write a program to prompt the user for hours and rate per hour to compute gross pay.

hours = input("Hours worked: ")
rate = input("Rate:")

pay = float(hours) * float(rate)
print(f"Total pay = {pay}")



#Excercise 3
#Write a program which prompts the user for a Celsius temperature,convert the temperature to Fahrenheit, and print out the converted temperature.

celcius = float(input("Input temperature in celcius: "))

fahrenheit = (celcius * 9/5) + 32

print(f"Fahrenheit is {fahrenheit}")'''



#Comparison operators and conditional statements
temp = 20
if temp > 30:
    print('Its warm')
    print('Drink water')
elif temp > 20:
    print('Its nice')
else:
    print('Its cold')

print('done')

age = 18
if age >= 18:
    print('This user is eligible')

else:
    print('This user is ineligible')
 ##



high_income = False
good_credit = True
student = True

if (high_income or good_credit) and not student:
    print('Eligible')

else:
    print("Ineligible")




#match
day = 5
match day:
    case 1:
        print('Monday')
    case 2:
        print("Tuesday")
    case 3:
        print("Wednesday")
    case 4:
        print("Thursday")
    case 5:
        print("Friday")
    case 6:
        print("Saturday")
    case 7:
        print("Sunday")
