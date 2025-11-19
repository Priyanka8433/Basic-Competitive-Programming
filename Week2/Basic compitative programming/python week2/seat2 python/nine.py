
# 9. Take an integer N as input. Your task is to calculate and print the sum of the digits of the 
# given number N. 
a=int(input("emter the number"))


num=abs(a)
sum=0
while num>0:
    digit=num%10
    sum+=digit
    num//=10
   
print(sum)