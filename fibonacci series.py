n = int(input("Enter a number where upto print series : "))
i=2
a=0
b=1
print("0",end=' ')
print("1",end=' ')
while i<n:
    c = a+b
    a=b
    b=c
    print(c,end=' ')
    i+=1

