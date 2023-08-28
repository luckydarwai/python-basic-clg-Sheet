month = int(input("Enter the month number 1-12 : "))
no_days=0


if month in (1,3,5,7,8,10,12):
    no_days=31 
elif month in (4,6,9,11):
    no_days=30
elif month==2:
    year = int(input("Enter the year : "))
    if(year % 4 ==0 ) and (not(year%100==0)) or (year%400==0):
        no_days=29
    else:
        no_days=28
else:
    print("please enter a valid month 1-12 : ")

print(no_days)

