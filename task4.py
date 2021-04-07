# 4. Print the sum of given lists:
# a) [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
# b) [1, 2, ‘3’, 4, 5, ‘6’, 7, 8, 9, 10]
# Note: Both lists should have same sum


a=[1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
sum=0
for i in a:
    sum=sum+i

print(f"Sum of a is {sum}")

total=0
b=[1, 2, '3', 4, 5, '6', 7, 8, 9, 10]
newList=list(map(int, b))
for j in newList:
    total=total+j

print(f"Sum of b is {total}")