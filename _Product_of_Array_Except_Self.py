n=int(input())
a=list(map(int,input().split()))
m=1
for i in range(n):
    s=1
    for j in range(n):
        if i!=j:
            s=s*a[j]
    print(s,end=" ")