def np(k):
    t=g=0
    while k:
        g=k%10
        t=(t*10)+g
        k=k//10
    return t
n=int(input())
a=1
d=n+1
e=n-1
while a:
    if np(d)==d and np(e)==e:
        a=0;
        break;
    elif np(d)!=d:
        d+=1
    elif np(e)!=e:
        e-=1
if d-n>n-e:
    print(e)
if d-n<n-e:
    print(d)
if d-n==n-e:
    print(e,d)
