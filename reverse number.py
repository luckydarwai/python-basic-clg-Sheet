# 14.	Write a C program to enter a number and print its reverse.
n = int(input('Enter a number : '))
while n!=0:
    a=n
    a=n%10
    print(a,end='')
    n//=10
print()
number= int(input('Enter a number : '))
r=0
while number!=0:
    res = number%10
    r=r*10+res
    number//=10
print("reverse :",r)