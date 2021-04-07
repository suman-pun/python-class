# import module(have to type module.something to access)
# or
# from module import area_of_rectangle as area(can print directly 
# like print(area_of_rectangle)
import module
from module import area_of_rectangle as area
from module import perimeter_of_rectangle as perimeter

length=16
breadth=20

print(module.area_of_rectangle(length, breadth)
print(module.perimeter_of_rectangle(length, breadth))



# #exception handlying
# try:
# 	a=int(input("Enter the number: ))
# 	b=int(input("Enter the number: ))

# 	print(f"Sum of {a} and {b} is {a+b}.")
# 	#print(n)
# except ValueError:
# 	print("Input must be  number")
# except NameError as err:
# 	print(err) # n not defined
# else:	
# 	print(f"Sum of {a} and {b} is {a+b}.")
# finally:
# 	print("Completed") 
# works at any case whether there is exception or not

# try:
#     pass#code
# except Exception:
#     pass
# except Exception:
#     pass
# else:
#     pass
# finally:
#     pass