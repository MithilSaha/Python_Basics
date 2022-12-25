person1 = {}
person1["Name"] = "Mr. A"
person1["Age"] = 34
print(person1)

person1["Status"] = "Alive"
print(person1)

person1["Status"] = "Dead"
print(person1)

del person1["Status"]
print(person1)

person2={
    "Name":"Mr. B",
    "Age":42,
    "Status":"Alive",
}
print(person2)

for key,value in person1.items():
    print(key + ":" + str(value))

for k in person2.keys():
    print(k + ":" + str(person2[k]))

for k in sorted(person2.keys()):
    print(k + ":" + str(person2[k]))

key1 = []
value1 = []
for k,v in person2.items():
    key1.append(k)
    value1.append(v)
print(key1)
print(value1)

print(list(person2.values()))

person3 = {}
person3 = {
    "Name":"Mr. C",
    "Hair":"Black",
    "Skin":"Black",
}

for v in person3.values():
    print(v)

for j in set(person3.values()):
    print(j)

person4 = {
    "Name":"Mr. D",
    "Age":32,
    "Status":"Alive",
}
person5 = {
    "Name":"Mr. E",
    "Age":45,
    "Status":"Dead",
}
person6 = {
    "Name": "Mr. F",
    "Age":65,
    "Staus":"Alive",
}

list1 = [person4,person5,person6]
print(list1)

person6 = {
    "Name":"Mr.G",
    "Hobby":["Cricket","Football"],
}
print(person6)

for k,v in person6.items():
    if type(v) is list:
        for x in v:
            print(person6["Name"]+" loves to play "+x)

food = {
    "Chicken":{
        "KFC":"Good",
        "Macdonald":"Medium",
        "Dominos":"Bad",
    },
    "Mutton":{
        "KFC":"Medium",
        "Macdonald":"Good",
        "Dominos":"Bad",
    },
}
print(food)

for k,v in food.items():
    for i,j in v.items():
        if j == "Medium":
            print(i+"'s "+k+" is "+j)


