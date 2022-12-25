list1 = list(range(1,6))

num = 1
while num < len(list1):
    print("Runnning")
    num+=1
print("Finish")

x = 1
while x < len(list1):
    print("started")
    if x == 4:
        print("BREAK")
        break
    x+=1
print("Finish")

while True:
    print("Started")
    break
print("BREAK")

x = 0
while x < len(list1):
    x +=1
    print("started")
    if x == 4:
        continue
        print("Continued")
print("Finish")

list2  = list(range(1,6))
while list2:
    x= list2.pop()
    print(x)

Ratings = {}
x =True
a = "Start Rating"
print(a)
while x:
    c = input("Do you want to give ratings, then 'Yes' other wise 'No': ")
    if c == "No":
        print("Thank you!")
        break
    while x:
        brand = input("Enter the name of brand: ")
        rating = input("Enter rating for the brand: ")
        Ratings[brand] = int(rating)
        b = input("Do you want to quit, then  type 'Yes' otherwise 'No': ")
        if b == "Yes":
            print("Thanks for your rating")
            x = False
        elif b == "No":
            continue
            
            
for k,v in Ratings.items():
    print("You have given "+k+" "+str(v)+" Ratings")