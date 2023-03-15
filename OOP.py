class Fruits:
    def __init__(self,type,colour,price):
        self.mytype=type
        self.mycolour=colour
        self.myprice=price
    def onyesha(self):
         print("My type is "+self.mytype, "its colour is "+self.mycolour,"its cost is ",self.myprice)
#CREATE AN OBJECT
myobj=Fruits("Red Grapes","Red",50)
myobj.onyesha()
object=Fruits("Apples","green",30)
object.onyesha()
another=Fruits("Mangoes","yellow",20)
another.onyesha()
example=Fruits("Oranges","orange",10)
example.onyesha()

class Employees:
    def __init__(self,name,age,salary):
        self.jina=name
        self.miaka=age
        self.malipo=salary
    def show(self):
        print("His/her name is "+self.jina,"He/she is aged "+self.miaka,"He/she is paid ",self.malipo +" per month")
information=Employees("Jacob","22","55000")
information.show()
information=Employees("Sara","23","55000")
information.show()
infor=Employees("Carlos","32","65000")
infor.show()
infor=Employees("Abigael","44","74000")
infor.show()