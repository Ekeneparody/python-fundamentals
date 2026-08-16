#FOR loop
from ctypes.wintypes import SMALL_RECT

'''for x in "banana":
    print(x)

for i in range(1,6):
    print(i)

for i in range(1,20):
    if i % 2 == 0:
        print(i)

for x in range(11):
    print('Hello world', x + 1, (x + 1) * '.')'''



#For else
'''successful = False
for x in range(3):
    print('Attempt')
    if successful:
        print('Successful')
        break
else:
    print('Attempted 3 times and failed')'''



#nested for loops
'''for x in range(5):
    for y in range(3):
        print(f"({x}, {y})")
#

#try
for x in "python":
    print(x * 2)
#try
for x in range(4):
    print("Python")'''
#

#
'''for x in [1,2,3,4]:
    print(x)'''
#

#Excercise
'''count = 0
for x in range(1, 10):
    if x % 2 == 0:
        count += 1
        print(x)

print(f'We have {count} even numbers')
'''#

#Finding average
'''total = 0
count = int(input("How many integers are being calculated:"))

for i in range(count):
    number = float(input("Enter a number:"))
    total = number + total

average  = total / count
print(f'The average is {average}')'''

#or

'''total = 0
count = 0

for i in range(4):
    number = float(input("Enter a number:"))
    total = number + total
    count = count + 1

average = total / count
print(f"The average is {average}")'''

#Finding the largest number
'''count = int(input("How many numbers are you entering: "))
largest = None

for i in range(count):
    numbers = int(input('Enter a number: '))

    if largest is None or numbers > largest:
        largest = numbers
print(F"The largest number is {largest}")'''


#Finding smallest number
'''count = int(input("How many numbers: "))
smallest = None

for i in range(count):
    numbers = int(input("Enter a number: "))

    if smallest is None or numbers < smallest:
        smallest = numbers

print(f'The smallest number is {smallest}')'''


#Counting even numbers
'''count = int(input("how many numbers: "))
even_count = 0
for i in range(count):
    number = int(input("Enter number: "))
    if number % 2 ==0:
        even_count = even_count + 1

print(f'They are {even_count} even numbers')'''

#Sum of positive numbers
'''count = int(input('How many numbers: '))
total = 0

for i in range(count):
    number = float(input("Enter a number: "))

    if number > 0:
        total = number + total

print(f"The sum of positive numbers: {total}")'''






'''Write a program that asks the user how many numbers they want to enter, 
then finds both the sum and average of only the positive numbers.'''

'''count = int(input("Enter how many numbers: "))
total = 0
positive_count = 0

for i in range(count):
    number = float(input("Enter a number: "))


    if number > 0:
        total += number
        positive_count += 1


print(f"The total number is {total}")
average = total / positive_count
print(f"The average is {average}")'''




'''Exercise: Count Positive, Negative, and Zero

Write a Python program that:

Asks the user how many numbers they want to enter.
Uses a for loop to receive the numbers.
Counts how many numbers are:Positive
Negative
Zero
Prints all three counts.'''



'''count = int(input('How many numbers: '))
negative_count = 0
positive_count = 0
zero_count = 0

for i in range(count):
    number = int(input('Enter a number: '))

    if number == 0:
        zero_count += 1

    elif number < 0:
        negative_count += 1

    elif number > 0:
        positive_count += 1

print(f"The total number of positive integers is {positive_count}")
print(f"The total number of negative integers is {negative_count}")
print(f"The total number of zero integers is {zero_count}")'''






'''Next Exercise: Number Statistics

Let's combine several things you've learned.

Write a program that asks the user how many numbers they want to enter, then calculates:

Total/sum of all numbers
Average of all numbers
Number of positive numbers
Number of negative numbers
Number of zeros'''


'''count = int(input("Enter the how many numbers: "))
total = 0
positive_count = 0
zero_count = 0
negative_count = 0



for i in range(count):
    numbers = float(input("Enter a number: "))
    total += numbers

    if numbers > 0:
        positive_count += 1

    elif numbers == 0:
        zero_count += 1

    else:
        negative_count += 1

average = total / count

print('Number Statistics')
print(f"The total is {total}")
print(f"The average is {average}")
print(f'There are {positive_count} positive integers')
print(f"There are {negative_count} negative integers")
print(f"There are {zero_count} zero integers")'''





'''Next Exercise: Find the Largest and Smallest

Now let's introduce a new concept.

Write a program that:

Asks the user how many numbers they want to enter.
Uses a for loop to receive the numbers.
Finds the largest number.
Finds the smallest number.
Prints both.'''


'''count = int(input('How many numbers: '))

largest = None
smallest = None

for i in range(count):
    number = int(input('Enter a number: '))

    if largest is None or number > largest:
        largest = number

    if smallest is None or  number < smallest:
        smallest = number

print(f"The largest number is {largest}")
print(f"The smallest number is {smallest}")'''




fruit = ["apple", 'pear', 'kiwi', 'bananna', 'orange']
for i in fruit:
    print(i)
    if i == 'bananna':
        break