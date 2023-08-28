# 1.	Write a C program to print all natural numbers from 1 to n. - using while loop
# 2.	Write a C program to print all natural numbers in reverse (from n to 1). - using while loop
n = int(input())
i=1
j=n
while i<n+1:
    print(i)
    i+=1
print()

while j>=1:
    print(j)
    j-=1