# 3. Write a program to calculate simple interest. Take principal, time and rate as user input.

# principal=int(input("Enter principal: "))
# time=int(input("Enter time: "))
# rate=int(input("Enter rate: "))
# simpleInterest=(principal*time*rate)/100
# print(f" Simple interest is {simpleInterest}")


# 4. Write a program to calculate Compound Interest and Compound Amount. Take principal, time
# and rate as user input

p=int(input("Enter principal: "))
t=int(input("Enter time: "))
r=int(input("Enter rate: "))
compoundAmount=p*(1+r/100)*t
compoundInterest=compoundAmount - p

print(f" Compound Amount is {compoundAmount}")
print(f" Compound interest is {compoundInterest}")