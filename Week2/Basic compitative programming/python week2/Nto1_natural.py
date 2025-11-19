#2. Write a program to print all Natural numbers from N to 1, where you have to take N as input from the user. 

N = int(input("enter the number: "))

if N < 0:
    print("enter the positive number greater than 0:")
else:

    for i in range(N, 0, 1):
        print(i, end= "") 

       
