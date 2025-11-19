# You are given two integers A and B. You have to find the value of A^B. 

A=int(input("enter first number"))
B=int(input("enter Second number"))
result=1
for i in range(B):
    result*=A
print(result)

# ans=ans*A
# ans=1*3=3
# ans=3*3=9