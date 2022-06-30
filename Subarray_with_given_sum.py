t=int(input())
while t:
    n,m=map(int,input().split())
    a=list(map(int,input().split()))
    s=zz=ii=jj=0
    mx=a[0]
    for i in range(n):
        for j in range(i,n):
            s=0
            for k in range(i,j+1):
                s=s+a[k]
                ##print(a[k],end=' ')
            if s==m:
                ii=i+1
                jj=j+1
                zz=1
                break
        if s==m:
            break
    if zz==1:
        print(ii,jj)
    else:
        print("-1")
    t-=1