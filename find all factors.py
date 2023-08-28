# 22.	Write a python program to find all factors of a number.
num = int(input("Enter the number : "))
factor=[]
for i in range(2,num+1):
    if num%i==0:
        factor.append(i)
print(factor)