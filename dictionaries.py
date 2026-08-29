#Dictionaries
car = {
    'brand' : 'Toyota',
    'year' : 2018,
    'model' : 'camry',
    'colors' : ['blue', 'green', 'black']
}

print(car)
print(len(car))

#accessing items(values)
print(car['colors'])
#or
print(car.get('model'))

#getting values
print(car.values())

#changing items
car['year'] = 2020

print(car.values())

#adding keys and values
car['seater'] = 4
print(car.values())

print(car.items())

#removing items
car.pop('seater')
print(car)

car.popitem()
print(car)


car = {
    'brand' : 'Toyota',
    'year' : 2018,
    'model' : 'camry',
    'colors' : ['blue', 'green', 'black']
}

print(car)

car['seater'] = 4
print(car)


#looping through a dictionary
for i in car:#printing the keys
    print(i)

for i in car:#printing the values
    print(car[i])

for i in car.keys():
    print(i)

for i in car.values():
    print(i)

#looping through both keys and values
for key, value in car.items():
    print(key, value)

carBrand = car.copy()
print(carBrand)

for key, value in carBrand.items():
    print(key, value)


#Nested dictionaries
myFamily = {
    'child1' :{
        'name' : 'James',
        'age' : 12,
    },
    'child2' : {
        'name' : 'David',
        'age' : 5,
    },
    'child3' : {
        'name' : 'Jonah',
        'age' : 10
    }
}

print(myFamily)
print(myFamily['child3']['name'])

for member, details in myFamily.items():
    print(member)
    for key, value in details.items():
        print(f"{key}: {value}")




'''students = {
    "Student1":{
        'name' : 'Sebastian',
        'age' : 20,
        'score' : 89
    },

    "Student2" : {
        'name' : "James",
        'age' : 19,
        "score" : 65
    },

    "Student3" : {
        'name' : 'Chris',
        'age' : 21,
        'score' : 90
    }
}

for student, details in students.items():
    print(student)
    for x, y in details.items():
        print(f"{x} : {y}")

for student, details in students.items():
    if details['score'] > 70:
        print(details['name'], ':', details['score'], 'got all As')


highest = None
for student,details in students.items():

    if highest is None or details['score'] > highest:
        highest = details['score']
        highest_name = details['name']
print(f"{details['name']} scored the highest:{highest}")

total = 0
count = 0
for student, details in students.items():
    total = details['score'] + total
    count += 1

average = total / count
print(f'The average is {average}')'''



#Looping through a dictionary of devices
devices = {
    'Device1':{'device': 'phone',
               'name': 'iphone 17',
               'color': 'black'

},
    'Device2':{
        'device' : 'laptop',
        'name' : 'Hp',
        'color' : 'ash'
    },
    'Device3':{
        'device' : 'camera',
        'name' : 'nikon',
        'color' : 'black'
    }
}

for device, details in devices.items():
    print(device)
    for key, value in details.items():
        print(f"{key} : {value}")















students = {
    'student1' :{
        'name' : 'James',
        'age' : '20',
        'department' : 'Computer Science',
        'score' : 65
    },
    'student2' :{
        'name' : 'Chris',
        'age' : 22,
        'department' : 'Medicine',
        'score' : 82,
    },
    'student3' :{
        'name' : 'David',
        'age' : 19,
        'department' : 'Optometry',
        'score' : 90
    }
}

for student, details in students.items():
    print(student)
    for key, value in details.items():
        print(f"{key} : {value}")
        print(f"The number of keys and values are {len(details)}")
        print(f"The number of students are {len(students)}")


total = 0
count = 0
for student, details in students.items():
    total += details['score']
    count += 1
average = total / count
print(f'The average score is {average}')

highest_score = None
for student, details in students.items():
    if highest_score is None or details['score'] > highest_score:
        highest_score = details['score']
        highest_name = details['name']
        highest_department = details['department']
print(f"{highest_name} scored the highest with a score of {highest_score} from the department of {highest_department}")

lowest_score = None
for student, details in students.items():
    if lowest_score is None or details['score'] < lowest_score:
        lowest_score = details['score']
        lowest_name = details['name']
        lowest_dep = details['department']

print(f"{lowest_name} scored the least with a score of {lowest_score} from the department of {lowest_dep}")

student_passed = 0
failed_student = 0
for student, details in students.items():
    if details['score'] < 70:
        failed_student += 1
    else:
        student_passed += 1


print(f"{failed_student} students failed")
print(f"{student_passed} students passed")
