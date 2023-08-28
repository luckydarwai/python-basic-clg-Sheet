
ap = float(input("Enter actual price :"))
sa = float(input("Enter sales amount :"))
amount=0
if(ap>sa):
    amount=ap-sa
    print("Total loss amount = %f"%(amount))
elif(sa>ap):
    print("Total profit amount = %f"%(amount))
else:
    print("No gain no loss")
