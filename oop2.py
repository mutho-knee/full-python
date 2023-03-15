class Person:
    def __init__(self,name,age):
        self.myname=name
        self.myage=age
    def habari(self):
        print("Hello my name is "+self.myname)

class Student(Person):
    def __init__(self,name,age,student_ID):
        super().__init__(name,age)
        self.mystudents=student_ID
        self.myage=age
        # self.myname=name
    def habari(self):
        super().habari()
        print("I'm a student with ID "+str(self.mystudents) +"and I am",17)

myname=Student("Maryann",17,54656)
myname.habari()
