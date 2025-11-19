#  Take an integer N as input and print the count of digits of that number. 

a = int(input("Enter the number: "))
count = 0
num=abs(a)
if num==0:
    count=1
else:
    while num>0:
        num//=10    
        count+=1
print(count)