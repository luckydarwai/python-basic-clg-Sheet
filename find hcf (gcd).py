# 24.	Write a python program to find HCF (GCD) of two numbers.
def hcf(a, b):
    # this is my python docstring 
    '''
    Now we are writing a docstring in the python programming language 
    by the help of this we work as a formal as also we can print the value of this docstring 
    by the help of .__doc__ this statement . thank you stay here for more updates. good day see you soon in the next upcoming program series which is given by instructor - mrs Rohit Bansal sir 
    '''
    if(b == 0):
        return a
    else:
        return hcf(b, a % b)
  
n1 = int(input())
n2 = int(input())
print("The gcd of {} and {} is : ".format(n1,n2) ,end="")
print(hcf(n1, n2))
print(hcf.__doc__)