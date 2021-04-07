# child class "IS A" parent class

# class Person:

#     def __init__(self, name, address, contact):
#         self.name = name
#         self.address = address
#         self.contact = contact

#     def walk(self):
#         print(f"{self.name} is walking.")

# class Student(Person):

#     def __init__(self, name, address, contact):
#         super().__init__(name, address, contact)

# class Teacher(Person):

#     def __init__(self, name, address, contact):
#         super().__init__(name, address, contact)

# s = Student("Ram", "Ktm", "98765432")
# # print(s.__dict__)
# s.walk()
# t= Teacher("Shyam", "Ktm", "123456789")
# t.walk()

#Overiding method
# class Bird:
#     def __init__(self, name):
#         self.name = name

#     def fly(self):
#         print(f"{self.name} is flying.")

# class Pigeon(Bird):
#     def __init__(self, name):
#         super().__init__(name)

# class Ostrich(Bird):
#     def __init__(self, name):
#         super().__init__(name)

#     def fly(self):
#         print(f"{self.name} could not fly.")

# class HummingBird(Bird):
#     def __init__(self, name):
#         super().__init__(name)

#     def fly(self):
#         super().fly()
#         print("It can also fly backward.")

# p = Pigeon("Robot")
# p.fly()
# ost = Ostrich("Horse")
# ost.fly()
# h = HummingBird("Tiny")
# h.fly()

