n=int(input())
lists=list(map(int,input().split()))
count=0
for id in lists:
    if id%2==0:
       print(n,end=" ")
       count+=1
if(count==0):
    print(-1)      