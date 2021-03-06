#forloops
list1 = [1,2,3,4,5]

for num in list1:
    print(num)
#1
#2
#3
#4
#5

#module
for num in list1:
    if num % 2 == 0:
        print(num)
#2
#4

list2 = [1,2,3,4,5,6,7,8,9,10]

for num in list2:
    if num % 2 == 0:
        print(num)
    else:
        print('Odd number')
# Odd number
# 2
# Odd number
# 4
# Odd number
# 6
# Odd number
# 8
# Odd number
# 10

for letter in 'This is a string.':
    print(letter)
# T
# h
# i
# s
#
# i
# s
#
# a
#
# s
# t
# r
# i
# n
# g
# .


mystring = 'hello'
mystring2 = 'hithere'

mylist = []

for letter in mystring:
    mylist.append(letter)

print(mylist)
#['h', 'e', 'l', 'l', 'o']

mylist = [letter for letter in mystring2]
print(mylist)
#['h', 'i', 't', 'h', 'e', 'r', 'e']

mylist = [x for x in 'word']
print(mylist)
#['w', 'o', 'r', 'd']

mylist = [x for x in range(0,11)]
print(mylist)
#[0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

mylist = [num**2 for num in range(0,11)]
print(mylist)
#[0, 1, 4, 9, 16, 25, 36, 49, 64, 81, 100]

mylist = [x for x in range(0,11) if x%2==0]
print(mylist)
#[0, 2, 4, 6, 8, 10]

mylist = [x**2 for x in range(0,11) if x%2==0]
print(mylist)
#[0,4,16,36,64,100]

celcius = [0,10, 20, 34.5]

fahrenheit = [( (9/5)*temp + 32) for temp in celcius]
print(fahrenheit)
#[[32.0, 50.0, 68.0, 94.1]


fahrenheit = []

for temp in celcius:
    fahrenheit.append(((9/5)*temp +32))

print(fahrenheit)
#[[32.0, 50.0, 68.0, 94.1]

results = [x if x%2==0 else 'ODD' for x in range(0,11)]
print(results)
#[0, 'ODD', 2, 'ODD', 4, 'ODD', 6, 'ODD', 8, 'ODD', 10]


mylist = []

for x in [2,4,6]:
    for y in [1,10,1000]:
        mylist.append(x*y)

print(mylist)
#[2, 20, 2000, 4, 40, 4000, 6, 60, 6000]

mylist = [x*y for x in [2,4,6] for y in [1,10,1000]]
print(mylist)
##[2, 20, 2000, 4, 40, 4000, 6, 60, 6000]

#usefulOperators
print('x' in [1,2,3])
