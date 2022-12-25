class Customer():
    def __init__(self,name,age,health_status):
        self.name = name
        self.age = age
        self.health_status = health_status
        self.premium = 0
    def customerDetails(self):
        if self.health_status == "Good":
            self.premium = 0
        elif self.health_status == "Moderate":
            self.premium = 5
        elif self.health_status == "Serious":
            self.premium = 10
        print(self.name.title()+"'s "+"age is "+str(self.age)+" and "+"health status is "+self.health_status.title())
        print("The premium for "+self.name+" is "+str(self.premium))
    def updateHealthStatus(self,hstatus):
        self.health_status = hstatus

jarry = Customer("jarry",23,"Good")
jarry.customerDetails()
jarry.updateHealthStatus("Moderate")
jarry.customerDetails()
print(jarry.health_status)