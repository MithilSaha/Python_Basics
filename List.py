list1 = ['apple','apple1','apple2']

print(list1[0])

list1[1] = 'apple3'
print(list1)

list1.append('apple4')
print(list1)

list1.insert(0,'apple5')
print(list1)

del list1[1]
print(list1)

x = list1.pop()
print(x)
print(list1)

y = list1.pop(0)
print(y)
print(list1)

list1.remove('apple3')
print(list1)

list2 = ['KFC','Dominos','Chillis','Macdonald']

list2.sort()
print(list2)

list2.sort(reverse=True)
print(list2)

print(sorted(list2))
print(sorted(list2,reverse=True))
print(list2)

list2.reverse()
print(list2)

for item in list2:
    print(item)

print(list(range(1,6)))
print(list(range(2,10,2)))

for num in range(1,6):
    print(num)

list3 = []
for number in range(1,6):
    list3.append(number+1)
print(list3)

list3 = [a for a in range(1,5)]
print(list3)

list4 = [b for b in range(1,7)]
print(list4)

print(list4[:4])

print(list4[2:6])

print(list4[4:])

print(list4[-4:])

list5 = list4[:]
print(list5)