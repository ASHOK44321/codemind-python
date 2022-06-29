def np(c):
    s=0
    if c!=1:
        for i in range(2,c):
            if(c%i==0):
                s=1
                break
    if s==0:
        return 1
    else:
        return 0
a=1
n=int(input())
d=n+1
e=n-1
if n>1 and np(n)==1:
    print('0')
elif n==0:
    print("2")
elif n==1:
    print('1')
else:
    while a:
        if np(d)==1 and np(e)==1:
            a=0
        elif np(d)!=1:
            d+=1
        elif np(e)!=1:
            e-=1
    if d-n>=n-e:
        print(n-e)
    else:
        print(d-n)