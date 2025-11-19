# Take a number A as input, print its multiplication table having the first 10 multiples.

a=int(input("enter number"))
i=0
for i in range(1,11):
    table=i*a
    print(a,"*",i,"=",table)