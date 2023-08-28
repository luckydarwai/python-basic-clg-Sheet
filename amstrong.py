n = int(input("Enter a number : "))
l=0
n1=n
n2=n
while n!=0:
    n=n//10
    l+=1
sum=0
while n1!=0:
    d = n1%10
    sum = sum + pow(d,l)
    n1=n1//10
    
if sum==n2:
    print(" an Armstrong")
else:
    print("Not an Armstrong")

