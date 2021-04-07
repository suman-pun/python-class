# 10. Take 15 user input as integer and print sum of all even numbers and odd numbers separately.

odd_sum=0
even_sum=0

for i in range(0,15):
    num=int(input("Enter the number: "))
    if num%2==0:
        even_sum=num+even_sum
        
    else:
        odd_sum=num+odd_sum

    print(f"Sum of even number is {even_sum}")
    print(f"Sum of odd number is {odd_sum}")