n=int(input())
a=list(map(int,input().split()))
c=s=z=0
for i in range(0,n):
    c=0
    for j in range(0,n):
        if a[i]==a[j]:
            if i!=j:
                a[j]=1000
            c+=1
    if a[i]==c and a[i]!=1000:
        s+=c
        z+=1
if z>=1:
    print("{:0.2f}".format(s/z))
else:
    print("-1")