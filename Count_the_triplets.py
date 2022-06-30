t=int(input())
while t:
    c=0
    n=int(input())
    a=list(map(int,input().split()))
    for i in a:
        for j in a:
            if i!=j:
                if i+j in a:
                    c+=1
    if c==0:
        print("-1")
    else:
        print(c//2)
    t-=1