class Customer():
    def __init__(self,name,age,health_status):
        self.name = name
        self.age = age
        self.health_status = health_status
        self.premium = ""
    def customerDetails(self):
        print(self.name.title()+"'s "+"age is "+str(self.age)+" and health status is "+self.health_status)
        if self.health_status == "Good":
            self.premium = Premium("Single")
        elif self.health_status == "Bad":
            self.premium = Premium("Regular")


class Premium():
    def __init__(self,prm):
        self.prm = prm
    def premiumDetails(self):
        print("The premium is "+self.prm)

class Employee(Customer):
    def __init__(self,name,age,health_status,salary):
        super().__init__(name,age,health_status)
        self.salary = salary
    def customerDetails(self):
        print(self.name.title()+"'s "+"age is "+str(self.age)+" and health status is "+self.health_status+" and salary is "+str(self.salary))
    def taxation(self):
        if self.salary > 100:
            tax = (self.salary)*0.1
            print(tax)
        else:
            print("You're not under taxation")


#jarry = Employee("jarry",32,"Good",90)
##jarry.taxation()

barry = Customer("barry",44,"Bad")
barry.customerDetails()
barry.premium.premiumDetails()



