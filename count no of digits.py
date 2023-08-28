# 10.	Write a program to count number of digits in a number

n = int(input('Enter a number '))
count=0
while n!=0:
    n = n//10
    count+=1
print(count)

# 11.	Write a  program to find first and last digit of a number.
# 12.	Write a program to find sum of first and last digit of a number.
def lastdigit(n):
  while n!=0:
    n=n%10
    return n
def firstdigit(n):
    while n >=10:
        n = n//10
    return n

n = int(input("Enter a number "))
print("First Digit : ",firstdigit(n),end=' ')
print("Last Digit : ",lastdigit(n))
    
print("Sum of first and Last digit is :",firstdigit(n)+lastdigit(n))

