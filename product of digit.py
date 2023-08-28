# 13.	Write a C program to calculate product of digits of a number.
n = int(input('Enter a digit : '))
product = 1
res = 1
while n!=0:
    a=n
    n//=10
    a%=10
    
    
    product *= a
print(product)
    
