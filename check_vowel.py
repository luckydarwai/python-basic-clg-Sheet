


str= input("Enter a alphabet : ")
list=['a','e','i','o','u','A','E','I','O','U']
if str.isalpha()==True:
  if str in list:
     print("Alphabet is vowel")
  else:
     print("Alphabet is consonant")
else:
    print("Not an alphabet")