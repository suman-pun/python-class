#Create two file module and test 
#module.py
# $ _name_ = _main_ if its in the main file and if it is 
# imported in another file it will be converted to module

sentence="This is a sentence"
PI=3.14

def area_of_rectangle(length,breadth):
	return length * breadth

def perimeter_of_rectangle(length, breadth):
	return 2 * (length + breadth)

# if _name__="__main_"
#	print(PI)
