#Excercise 1
'''Rewrite your pay computation to give the employee 1.5 times the
hourly rate for hours worked above 40 hours.'''

'''hours = float(input("Enter hours: "))
rate = 10
pay = hours * rate



if hours >= 40:
    print(f"The total pay = {(hours * 1.5) * rate} ")
else:
    print(pay)'''



#Excercise 2
'''Build a grading system'''

'''score = float(input('What is your score:'))

if score >= 90:
    print("A.\nPerfect score")
elif score >= 80:
    print("B")
elif'''


#nested if statements
'''age = float(input('Enter your age: '))
has_licence = True

if age >= 18:
    if has_licence:
        print('You can drive')
    else:print('You need a licence')
else:print('You are not old enough')'''


#Example
score = float(input("Enter your score: "))
attendance = float(input("Enter your attendance: "))
has_submitted = True

if score >= 80:
    if attendance >= 70:
        if has_submitted:
            print('Passed Outstandingly')

        else:print("Has a missing assignment")
    else:print('Passed but low attendance')
else:print("Failed")

