# class and object
# Inheritance
# Encapsulation
# Polymorphism
# Abstraction
# Accesor and Mutator function (Getter and function)

#1. class and object , noun
#=>state (charactertics, property) ,adjective
#=>behaviour (action, function), verb

class Car:
    #init intilaizer function to initialze variale from object
    def __init__(self, name, color, year): #self is the object of the class, first parameter
        self.name= name  #sefl.name is attribute of object, name is parameter
        self.color= color
        self.year= year
    
    def start(self):
        print(f"{self.name} started.")
    
    def stop(self):
        print(f"{self.name} stopped.")

c=Car("BMW", "BLACK", "2021")
print(c.__dict__)