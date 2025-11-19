# 5. Write a program to find the sum of all Natural numbers from 1 to N, where you have to take N as 
# input from user 

a=int(input("enter the number"))
sum=0
for i in range(1,a+1):
    sum+=i
    print(sum)