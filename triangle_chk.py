a = int(input("Enter side 1 : "))
b = int(input("Enter side 2 : "))
c = int(input("Enter side 3 : "))
sum=0

if a>0 and b>0 and c>0:
    sum=a+b+c
    if sum==180:
        print("valid Triangle ")
    else:
        print("Invalid Triangle ")
else:
    print("Invalid Triangle ")