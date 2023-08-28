
n = int(input('Enter the number : '))
flag = 0
if n==0 or n==1:
    flag = 1
else:
  for i in range(2,n//2):
       if n%i==0:
        flag=1 
        break
if flag == 0:
    print('prime')
else:
    print("Not prime")