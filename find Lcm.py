# 25.	Write a C program to find LCM of two numbers.
def lcm(n1,n2):
    if n1>n2:
        greater = n1
    else:
        greater = n2
    while(1):
            # 60 % 12 == 0   and  60 % 10 == 0
        if (greater%n1==0) and (greater%n2==0):
            lcm = greater
            break
        greater +=1
    return lcm
    
        
n1 = int(input())
n2 = int(input())
print(lcm(n1,n2))
print(12%10)