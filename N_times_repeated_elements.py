n=int(input())
a=list(map(int,input().split()))
k=int(input())
c=s=zap=0
x=z=a[0]
for i in range(0,n):
    c=0
    for j in range(0,n):
        if a[i]==a[j]:
            if i!=j:
                a[j]=1000
            c+=1
    if c==k and a[i]!=1000:
        print(a[i],end=" ")
        zap+=1 
if zap<1:
    print("-1")