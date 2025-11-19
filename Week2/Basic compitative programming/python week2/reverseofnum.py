a= int(input("enter the number: "))
if a < 0:
    rev = -int(str(-a)[::-1])
else:
    rev = int(str(a)[::-1]) 

print(" the Reverse of {a} is ", {rev})
