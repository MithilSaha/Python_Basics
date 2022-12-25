list1 = [1,2,3,4,5,6]
for x in list1:
    if x>3:
        print('Pass')
    else:
        print('Fail')

if 4 in list1:
    print('Present')
else:
    prin('Absent')

if 1 not in list1:
    print('Ok')
else:
    print('Not Ok')


for x in list1:
    if x>5:
        print("More than 5")
    elif x>3:
        print("More than 3")
    else:
        print("Less than 3")

list2 = list1[:3]

for x in list1:
    if x in list2:
        print("Have")
    else:
        print("Not Have")

