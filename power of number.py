# Enter base: 2
# Enter exponent: 5
# 2 ^ 5 = 32	
# 21.	Write a python program to find power of a number using for loop

num=int(input("Enter a number : "))
power=int(input("Enter a power of the number : "))
res=1
for i in range(power):
    res=res*num
    
    
print(res)