#Filehandle.py
#write,append,read

#write, w
f=open("test.txt","w")
f.write("Hello,I am Python Here.\n")
f.close()


#append, a
f=open("test.txt","a")
f.write("Hello there, I am new Python")
f.close()

#read, r
f=open("test.txt", "r")
print(f.read())
f.close()

#read gives all data inside file
#readline read only single first line
#readlines reads all line and return in list