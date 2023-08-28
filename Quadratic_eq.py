from cmath import sqrt

a =int(input("Enter a : "))
b =int(input("Enter b : "))
c =int(input("Enter c : "))
d=((b**2)-(4*a*c))
x=(-b+sqrt(d))/(2*a)
y=(-b-sqrt(d))/(2*a)

print(x,y)
