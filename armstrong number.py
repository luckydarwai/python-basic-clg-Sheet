num = input(" Enter a number : ")
l=len(num)
res = 0
for i in num:
    res =res+((int(i))**l)
print(res)
if int(num)==res:
    print("armstrong number")
else:
    print("no")
