# 2. Take five user input, cast into integer. Print count of all the duplicate numbers.
# # a = [1, 2, 3, 4, 5] => {1:1, 2:1, 3:1, 4:1, 5:1}
# # b = [1, 2, 2, 3, 3] => {1:1, 2:2, 3:2}



a=[]
duplicateElement={}
for i in range(0,5):
    num=int(input("Enter the number: "))
    a.append(num)
    duplicateElement[num]=a.count(num)
print(duplicateElement)  

