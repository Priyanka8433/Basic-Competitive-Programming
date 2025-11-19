# n = int(input("Enter the number"))

# for i in range(n, 0, -1):
#     for j in range(n-i):
#         print(" ", end=" ")
#     for k in range(i):
#         print("*", end=" ")
#     print()


# n=int(input())
# for i in range(1,n+1):
#     for j in range(1,n+1):
#         if j==1 or j==n:
#             print("*",end=" ")
#         else:
#             print("-",end=" ") 
#     print()   

# n=int(input())
# for i in range(1,n+1):
#     for j in range(n-i):
#         print(" ",end=" ")
#     for j in range(2*i-1):
#         print("*",end=" ")
#     print()    

#     for i in range(4,0,-1):
#     for j in range(n-i):
#         print(" ",end=" ")
#     for j in range(2*i-1):
#         print("*",end=" ")
#     print()  

n=int(input())
sum=1
for i in range(1,n+1):
    for j in range(i):
        print(sum,end=" ")
        sum +=1
    print()