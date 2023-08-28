while 1:
    year = int(input("Enter the year : "))
    if year==0:
        break
    if year%4==0:
        if year%4==0 and year%100 !=0:
            print("leap year")   
        elif year%100 ==0 and year %400==0:
            print("leap year") 
        else:
            print("Not leap year")  
    else:
        print("Not leap year")