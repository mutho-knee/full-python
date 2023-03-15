class Animal:
    def __init__(self,name):
        self.myname=name

    def talk(self):
        raise NotImplementedError("Subclass must implement abstract method")

class cat(Animal):
    def talk(self):
        return "Meow"

class dog(Animal):
    def talk(self):
        return "Barks"

class cow(Animal):
    def talk(self):
        return "Moows"

class lion(Animal):
    def talk(self):
        return "roars"

class hyena(Animal):
    def talk(self):
        return "laughs"

paka=cat("Misty")
mbwa=dog("Boscomref")
ngombe=cow("Mukami")
simba=lion("Softy")
fisi=hyena("Kayesa")

print(paka.myname+" :"+paka.talk())
print(mbwa.myname+" :"+mbwa.talk())
print(ngombe.myname+" :"+ngombe.talk())
print(fisi.myname+" :"+fisi.talk())
print(simba.myname+" :"+simba.talk())