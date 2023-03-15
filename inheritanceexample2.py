class Magari:
    def __init__(self,make,model,year):
        self.mymake=make
        self.mymodel=model
        self.myyear=year
    def kuanzishaengine(self):
        print(f"{self.mymake} {self.mymodel}{self.myyear} started")

class Toyota(Magari):
    def __init__(self,make,model,year,num_doors):
        super().__init__(make,model,year)
        self.mynum_door=num_doors

    def kuanzishaengine(self):
        print(f"{self.mymake}{self.mymodel}{self.myyear}car with {self.mynum_door}doors")
gari=Toyota("Premio","Saloon,",2023,5)
gari.kuanzishaengine()

class Bikes:
    def __init__(self,make,model,year):
        self.mymake=make
        self.mymodel=model
        self.myyear=year
    def mybikes(self):
        print(f"{self.mymake}{self.mymodel}{self.myyear}")

class Honda(Bikes):

        super().__init__(make,model,year)
        self.mycc=cc
    def mybikes(self):
        print(f"{self.mymake}{self.mymodel}{self.myyear}bike with {self.mycc} CC")
nduthi=Honda("Duggati"," speed bike ",2023,600)
nduthi.mybikes()

class People:
    def __init__(self,name,age,gender):
        self.myname=name
        self.mygender=gender
        self.myage=age
    def real(self):
        print(f"{self.myname}{self.myage}{self.mygender}")

class she(People):
    def __init__(self,name,age,gender,location):
        super().__init__(name,age,gender)
        self.mylocation=location
    def real(self):
        print(f"Hey,my name is {self.myname} I am a {self.mygender} aged {self.myage} I live in {self.mylocation}")
jina=she("Santia",18,"girl","Kiri"
                            "nnnnn  aini")
jina.real()
