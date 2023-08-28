def isprime(n):
    for j in range(2,n):
        if n%j==0:
            return False
    return True
        
       
        
n = int(input())
list =[]
for i in range(2,n+1):
    if(isprime(i)):
        list.append(i)
           
print(list)          
      
           
   
         
    
