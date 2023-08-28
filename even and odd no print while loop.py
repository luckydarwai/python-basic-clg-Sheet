# 4.	Write a C program to print all even numbers between 1 to 100. - using while loop
# 5.	Write a C program to print all odd number between 1 to 100.
# 6.	Write a C program to find sum of all natural numbers between 1 to n.
# 7.	Write a C program to find sum of all even numbers between 1 to n.
# 8.	Write a C program to find sum of all odd numbers between 1 to n.

n = int(input())
i = 1
sumodd=0
print('odd values')
while i<n:
    print(i,end=' ')
    sumodd += i
    i +=2
print()
print(sumodd)
print()
j = 2
sumeven=0
print('Even values')
while j<n:
    print(j,end=' ')
    sumeven+=j
    j+=2
print()
print(sumeven)
