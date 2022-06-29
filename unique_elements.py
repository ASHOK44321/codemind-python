n=int(input())
a=list(map(int,input().split()))
c=0
for i in range (0,n):
    c=0
    for j in range (0,n):
        if i!=j:
            if a[i]==a[j]:
                a[j]=1000
    if c==0 and a[i]!=1000:
        print(a[i],end=" ")