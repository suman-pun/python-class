# * (single *retruns in tuple) accept all agruments incase parameter are not equal
# def func(*args):
# 	print(args)

# func(1, 2, "python", "php")


# ##**returns vaule in dictionary

# def func_new(**kwargs):
#     print(kwargs)

# func_new(name="Ram", contact="2342")



# def function_values(*args,**kwargs):
# 	print(args,kwargs)



# function_values(1,2,3,4,name="HARI",contact="1132")


#function reference 
# def welcome():
# 	print("Welcome Ram")

# w=welcome
# w() #same as welcome()



def welcome(name):
	print(f"Welcome {name}")

def namaste(name):
	print(f"Namaste {name}")

def greet(w,name):
	w(name)

greet(welcome,"Ram")
greet(namaste, "Shyam")