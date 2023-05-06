print("hello")
thislist = ['apple', 'cherry', 'banana']
print(thislist)
print(len(thislist))
print(type(thislist))
thislist= list(('apple', 'banana', 'cherry'))
print(thislist)
print(thislist[1])
if "mango" in thislist:
    print("yes, 'mango' is in the list")
else:
    print("No, 'mango' is not in the list")
thislist[1:2]= ['mango', 'orange']
print(thislist)
thislist.insert(2, 'watermelon')
print(thislist)
thislist.append('strawberry')
print(thislist)
Temperate=['yam', 'coconut']
thislist.extend(Temperate)
print(thislist)
thislist.remove('watermelon')
print(thislist)
thislist.pop(1)
print(thislist)
del thislist[4]
print(thislist)
thislist.clear()
print(thislist)

thislist = ['apple', 'cherry', 'banana', 'mango']
for x in thislist:
    print(x)
    thislist.sort()
    print(thislist)


    numbers= ['33', '84', '67', '99']
    numbers.sort()
    print(numbers)

    thislists=['apple', 'cherry', 'banana']
    thislists2=thislists.copy()
    thislists2.append('orange')
    print(thislists)
    print(thislists2)

# for loops in python list
students = ['alex', 'bola', 'david']
for newstudents in students:
    if 'alex' in newstudents:
        print('alex is part of the list')
        
for x in range(len(students)):
            print(x)


