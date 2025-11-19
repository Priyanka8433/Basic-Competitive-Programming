# 1. Write a program that takes a positive integer N as input from the user and prints all natural numbers 
#numbers from 1 to N, with each number followed by a space.

N = int(input("Enter the number: "))

if N <= 0:
    print("Please enter a positive integer greater than 0.")
else:
    for i in range(1, N + 1):
        print(i, end=" ")

