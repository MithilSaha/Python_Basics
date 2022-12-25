def helloWrold():
    print("Hello World!")

helloWrold()

def food(food1,food2):
    print(food1)
    print(food2)

food("Pizza","Icecream")

def summation(a,b,c):
    d = a+b+c
    return d

x = summation(1,2,3)
print(x)

def work1(a,b,c):
    e = work2(a,b) + c
    return e

def work2(x,y):
    z = x-y
    return z

result = work1(10,6,4)
print(result)

def person(name,age,status):
    person_detail = {"Name":name,"Age":age,"Status":status}
    return person_detail

person1 = person("Mr. XYZ",32,"Alive")
print(person1)

def number_list(numbers):
    x=0
    for number in numbers:
        x = number + x
    return x

Numbers = list(range(1,6))
result = number_list(Numbers)
print(result)

def rating(brand,*ratings):
    y=0
    for rate in ratings:
        y = rate + y
    print(brand + "'s" + " total ratings is " + str(y))

rating("KFC",1,2,3,4)
    
def all_ratings(brand,**ratings):
    z = 0
    for k in ratings.keys():
        if k == "Food":
            print(brand + "'s" + " food rating is " + str(ratings[k]))
        if k == "CC":
            print(brand + "'s" + " Customer Care rating is " + str(ratings[k]))
        z = ratings[k] + z
    print(brand + "'s"+ " total rating is " + str(z))

all_ratings("KFC",Food=6,CC=5)

def multpl(a,b,c,
        d,e,f):
    return a*b*c*d*e*f

x = multpl(2,4,3,2,4,3)
print(x)