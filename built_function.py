#built in function, higher order function(hof)
#map and filter
#map(func, iterable_object)

def a(x1,x2,x3):
	return x1+x2+x3

a=lambda x1,x2,x3:x1+x2+x3
print(a(6,7,8))

#map example

a=[2,4,6,8,10,12]
b=map(lambda n:n+1,a)#n= variable, n+1=return type
print(list(b))
#output =[3, 5, 7, 9, 11, 13]

#task , Name should be in Captital,e.g Ram

namelist=["ram", "shyam","hari", "geeta", "harry"]
result=list(map(lambda n:n.title(),namelist))
print(result)

#task2 , replacing - to @ of the given list
email=["1-gmail.com", "2-gmail.com", "3-gmail.com","4-
gmail.com"]
res=list(map(lambda n:n.replace("-", "@"), email))
print(res)

#Filter(func,iterable_object),if true returns value but incase 
# of map it returns boolean value

a=[1,2,3,4,5,6,7,8,9,10]
even=list(filter(lambda n:n%2==0, a))
print(even)
#task

emailList=["1@gmail.com", "2@gmail.com", "3@gmail.com","4@gmail.com"]
email=list(filter(lambda n:n.endswith("gmail.com"), emailList))
print(email)
