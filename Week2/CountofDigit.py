# N = int(input("Enter number: "))

# count = 0
# while N > 0:
#     N //= 10
#     count += 1

# print("Number of digits =",count)


N = int(input("Enter number: "))
digit=int(input())
count = 0
while N > 0:
    Digit=N%10
    N //= 10
    if digit==Digit:
        count+=1

print("Number of digits =",count)


