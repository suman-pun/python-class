
#Nested function

#calling inner_func() inside inner func
def main():
	def inner_func():
		print("I am inner fucntion")
	inner_func()

main()

#calling inner function globally

def main():
	def inner_func():
		print("I am inner fucntion")
	return inner_func

in_func=main()
in_func()

def main(n):
	def addition(a, b):
		return a + b
	def subtraction(a, b):
		return a - b
	if n==1:
		return addition
	elif n==2:
		return subtraction

add=main(1)
print(add(5,5))
sub=main(2)
print(sub(7, 2))


#global / local scope

num=10 #immutable/not chanable object

def main_fucntion():
	global num # if we want to access mutable object inside function as local variable
	num=num+1
	print(num)

main_function()
 

#mutable/changeable object

aList=[1, 4]
def main():
	aList.append(5) # no need to make global since it is (list) chanable object

print(aList)
main()
print(aList)


#nonlocal function to access local variable outside inner function but inside main function

num=10 #global variable
def main():
	num=15 #nonlocal variable
	def inner_func():
		nonlocal num
		num=num+1				
		print(num)
	inner_func()

main()