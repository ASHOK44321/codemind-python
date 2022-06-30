t=int(input())
while t:
    n,m=map(int,input().split())
    a=list(map(int,input().split()))
    b=list(map(int,input().split()))
    c=[0]*(n*m)
    c=a+b
    c.sort()
    print(*c,sep=" ")
    t-=1