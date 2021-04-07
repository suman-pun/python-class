#OOP

# class Laptop:
# 	def __int__(self, brand, color, ram="2GB"):
# 		#instance variable=self object ko attribute
# 		self.brand=brand
# 		self.color=color
# 		self.ram=ram
# 	#instance method
# 	def reboot(self):  #object passing (l and d)
# 		print(f"{self.brand} laptop is rebooting")


# l=Laptop("Lenovo", "Black", "16GB")
# print(l.ram)

# d=laptop("Dell","White")
# print(d.ram)

# l.reboot()
# d.reboot()


class Calculator:

	def __init__(self, num1, num2):
		self.num1=num1
		self.num2=num2

	def add(self):
		return self.num1 + self.num2

	def differece(self):
		return self.num1 - self.num2

	def product(self):
		return self.num1 * self.num2

	#staticmethod, if we dont  want to use class oject
	
	@staticmethod
	def square_root(num):
		return num**0.5

c = Calculator(20, 10)
print(c.add())
print(Calculator.square_root(100))  # can use object as well (c.square_root())


# class Student:
	
# 	collage_name="ABC College"  #class or static variable
# 	def __int__(self, id, name, address):
# 		self.id=id
# 		self.name=name
# 		self.addres=address
# s=Student("002", "Ram", "Ktm")
# print(s.collage_name)
# print(s.__dict__)
# print(Student.collage_name)