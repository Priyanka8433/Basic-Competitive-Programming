
num=int(input("enter the number"))
original=num
reverse=0
while num>0:
    digit=num%10
    reverse=reverse*10+digit
    num//=10
if original==reverse:   
   print("palindrome")
else:
    print("not palindrome")   