t=int(input())
while t:
    n=int(input())
    a=list(map(int,input().split()))
    a.sort()
    c=0
    ##print(n)
    ##print(*a,sep=" ")
    for i in range(1,n):
        if i!=a[i-1]:
            c=1
            print(i)
            break
    if c==0:
        d=a[n-2]
        print(d+1)
    t-=1