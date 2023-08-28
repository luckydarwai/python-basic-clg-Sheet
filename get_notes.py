amt = int(input("Enter the amount : "))
note1=note2=note5=note10=note20=note50=note100=note200=note500=note2000=0

if amt>=2000:
    note2000 = amt//2000
    amt = amt%2000
    print("Note 2000 : ",note2000)
    
if amt>=500:
    note500=amt//500
    amt=amt%500
    print("Note 500 : ",note500)
    
if amt>=200:
    note200=amt//200
    amt=amt%200
    print("Note 200 : ",note200)
    
if amt>=100:
    note100=amt//100
    amt=amt%100
    print("Note 100 : ",note100)
    
if amt>=50:
    note50=amt//50
    amt=amt%50
    print("Note 50 : ",note50)
    
if amt>=20:
    note20=amt//20
    amt=amt%20
    print("Note 20 : ",note20)
  
if amt>=10:
    note10=amt//10
    amt=amt%10
    print("Note 10 : ",note10)
   
if amt>=5:
    note5=amt//5
    amt=amt%5
    print("Note 5 : ",note5)
    
if amt>=2:
    note2=amt//2
    amt=amt%2
    print("Note 2 : ",note2)
   
if amt>=1:
    note1=amt//1
    amt=amt%1
    print("Note 1 : ",note1)
    