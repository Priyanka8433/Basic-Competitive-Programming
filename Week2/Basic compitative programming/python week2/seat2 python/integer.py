A = [int(x) for x in input("Enter list elements (space separated): ").split()]
B = int(input("Enter target sum: "))

found = False
for i in range(len(A)):
    for j in range(i + 1, len(A)):
        if A[i] + A[j] == B:
            print(f"Pair found: ({A[i]}, {A[j]})")
            found = True
            break
    if found:
        break

if not found:
    print("No pair found")



arr=[11,12,13,14,15]
N=len(A)
count=0
for i in range(N):
  sum += A[j]


# a=3
# c=[2,2,2]
# b=1

# a=5
# b=12
# c=21345

