basic_salary=float(input("Enter basic salary "))
da=hra=0
if basic_salary<=10000:
    da=basic_salary*0.8
    hra=basic_salary*0.2
elif basic_salary<=20000:
    da=basic_salary*0.9
    hra=basic_salary*0.25
else :
    da=basic_salary*0.95
    hra = basic_salary*0.30

gross_salary=da+hra
print("Gross salary is : %f"%(gross_salary))
