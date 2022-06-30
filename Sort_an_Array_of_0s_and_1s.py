a=int(input())
arr=list(map(int,input().split()))
c=arr.count(0)
for i in range(c):
    print(0,end=" ")
for i in range(len(arr)-c):
    print(1,end=" ")