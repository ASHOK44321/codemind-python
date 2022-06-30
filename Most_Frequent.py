n=int(input())
a=list(map(int,input().split()))
a.sort()
c=0
m=d=0
for i in range(n):
    c=0
    for j in range(n):
        if a[i]==a[j]:
            c+=1
    if c>m:
        d=a[i]
        m=c
print(d)