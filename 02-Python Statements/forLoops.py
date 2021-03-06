list1 = [1,2,3,4,5,6,7,8,9,10]

for num in list1:
    print(num)
# 1
# 2
# 3
# 4
# 5
# 6
# 7
# 8
# 9
# 10

#module
print(17 % 5)
#2
print(10 % 3)
#1
print(18 % 7)
#4
print(4 % 2)
#0

for num in list1:
    if num % 2 == 0:
        print(num)
# 0
# 2
# 4
# 6
# 8
# 10

for num in list1:
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

list_sum = 0

# for num in list1:
#     list_sum = list_sum + num
#
# print(list_sum)
#55

for num in list1:
    list_sum = list_sum + num

    print(list_sum)
# 1
# 3
# 6
# 10
# 15
# 21
# 28
# 36
# 45
# 55

#Start sum at zero
list_sum = 0

for num in list1:
    list_sum += num

print(list_sum)
#55

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

#For loop within a tuple

tup = (1,2,3,4,5)
for t in tup:
    print(t)
# 1
# 2
# 3
# 4
# 5
list2 = [(2,4),(6,8),(10,12)]

for tup in list2:
    print(tup)
# (2, 4)
# (6, 8)
# (10, 12)

#Now with unpacking!
for (t1,t2) in list2:
    print(t1)
#2
#6
#10

d = {'k1':1,'k2':2,'k3':3}

for item in d:
    print(item)
# k1
# k2
# k3

for k,v in d.items():
    print(k)
    print(v)
# k1
# 1
# k2
# 2
# k3
# 3
