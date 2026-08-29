#Lists
fruits = ['Apple', 'Kiwi', 'Orange', 'Pineapple',"Watermelon", 'melon']
print(fruits[0])
print(len(fruits))

#List constructor
fruitlist = list(('apple', 'banana', 'cherry'))
print(fruitlist)

#checking if item exist
if "apple" in fruitlist:
    print('Yes, apple is in fruit list')

#Looping through a list
for i in fruits:
    print(i)

#Changing list items
fruitlist[1] = "blackcurrant"
print(fruitlist)
print(fruits)
fruits[1:3] = ['grape', 'pawpaw','biscuit']
print(fruits)

#Inserting items
fruits.insert(0, 'nut')
print(fruits)

#Adding items to a list
fruits.append('groundnut')
print(fruits)

#Joining lists
fruits.extend(fruitlist)
print(fruits)

#remove item
fruits.remove('apple')
print(fruits)

#or
fruits.pop(-3)
print(fruits)

#looping through a list
for i in range(len(fruits)):
    print(i)

newlist = []

for x in fruits:
    if 'a' in x:
        newlist.append(x)
print(newlist)

##

carlist = ['Avalor', 'aventador', 'Bugatti', 'chevrolet']
a_carlist = []

for x in carlist:
    if x.startswith('a') or x.startswith('A'):
        a_carlist.append(x)
print(a_carlist)

for x in a_carlist:
    print(f'This is {x}')
##
fruits.sort() #sorts the original list
fruits = sorted(fruits) #creates and returns a new sorted list
print(fruits)
print(fruits)

#case insensitive sorting
fruits.sort(key= str.lower)
print(fruits)
fruits.reverse()
print(fruits)

#Sorting numbers in ascending numbers
numbers = [10,50,80,78,68,94,86,54,27,57,45]
numbers = sorted(numbers)
print(numbers)
numbers.sort()
print(numbers)

#Sorting numbers in descending numbers
numbers.sort(reverse=True)
print(numbers)


#Copying a list
names = ['Udoka', 'Chris', 'Ihu']
people = names.copy()
print(people)
print(names)

