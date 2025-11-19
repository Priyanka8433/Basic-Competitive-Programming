# n = int(input("Enter the no of rows"))

# for i in range(n):
#     for j in range(n - i):
#         print("*", end="")
#     for j in range(2 * i):
#         print(" ", end="")
#     for j in range(n - i):
#         print("*", end="")   
#     print()

# n=int(input())
# for i in range(1,n+1):
#     for j in range(1,11):
#         if j<=6-i or j>=5+i:
#             print('*',end="")
#         else:
#             print(" ",end="")
#     print()     
# for i in range(n,0,-1):
#     for j in range(1,11):
#         if j<=6-i or j>=5+i:
#             print("*",end="")
#         else:
#             print(" ",end="")
#     print()           


# n=int(input())
# for i in range(n):
#     for j in range(n):
#         if i==0 or i==n-1:
#             print("*",end=" ")
#         elif j==0 or j==1:
#             print("*",end=" ")    
#         else:
#             print(" ",end=" ")
#     print()       

# n=int(input())
# for i in range(1,n+1):
#         if i==3:
#             print("*",end=" ")  
#         else:
#             print("* *",end=" ")
#         print()      
# 
# n=int(input())
# for i in range(1,n+1):
#     for j in range(2*i-1):
#          print("*",end=" ")
#     print()

# n=5
# for i in range(n,0,-1):
#     for j in range(2*i-1):
#         print("*",end=" ")
#     print()


# n=5
# for i in range(n,0,-1):
#     for j in range(i):
#         print("*",end=" ")
#     print()
# for i in range(2,n+1):
#     for j in range(i):
#         print("*",end=" ")
#     print()    
n=6
for i in range(1,n+1):
        if i==4 :
            print("*")
        else:
            print("* * *")          