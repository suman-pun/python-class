#oop 3rd day

class Product:
	
	def __init__(self, name, price):
		self.name=name
		self.price=price #name mangaling 		
		#"_Product__price" _Classname__attbute

	@property
	def price(self):
		return self.__price
	
	@price.setter
	def price(self, price):
		if price > 0:
			self.__price=price

	def __str__(self):#special function, it will access 	
	#object lai redeable garna help garxa
		return f"{self.name}=>{self.price}"


	# #def get_price(Self):
	# 	return self.__price

	# #def set_price(Self):
	# 	if price > 0:
	# 		self.__price=price

	#operator overloading
	def __eq__(self, obj):
		return self.__price=obj.__price


p=Product("Pant", 1600)
t=Product("T-shirt",1600)
print(p==t)
#print(p.get_price())
#p.set_price(100)
#print(p.get_price())
print("Initial value",p.price)
p.price=1900
print("Final value", p.price)
print(p)