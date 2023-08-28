a = int(input("Enter side 1 : "))
b = int(input("Enter side 2 : "))
c = int(input("Enter side 3 : "))
if a==b and b==c and c==a:
    print("Equilateral triangle")
elif a==b or b==c or c==a:
    print("isosceles triangle ")
else:
    print("Tringle is scalene")