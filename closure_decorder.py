# #closure

# def multiplier(n):
# 	def times(a):	
# 		return a*n
# 	return times

# times3=multiplier(3)
# times5=multiplier(5)
# #del multiplier #works even after deleting which is call 
# closure 
# print(times5(10))

# #Decorators,must be in same lines like 9 and 10 or any work 
# #between these two , it wont work.

# def decorate_function(func):
# 	def wrapper():
# 		print("Nice to see you.")
# 		func()
# 		print("Welcome again.")
# 	return wrapper

# @decorate_function
# def greet():
# 	print("Welcome Home.")

# greet()


# def smart_decorate(func):
# 	def wrapper(num1, num2):
# 		if num2==0:
# 			return "Could not divisible by zero"
# 		else:
# 			return func(num1, num2)
# 	return wrapper

# @smart_decorate
# def division(num1,num2):
# 	return num1/num2

# print(division(10,10))
# print(division(2,0))

def smart_decorate(func):
	def wrapper(num1, num2):
		print("Below is decorate function")
		return func(num1, num2)
		
	return wrapper

@smart_decorate
def calculator(num1, num2):
	return num1 + num2

print(calculator(5, 6))
