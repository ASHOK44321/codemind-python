n=int(input())
a=[0]*n
d=k=e=b=0
for i in range(2,n+1):
    d=0
    for j in range(2,i):
        if i%j==0:
            d=1
            break
    if d==0:
        a[k]=i
        k+=1
for i in range(k-1,-1,-1):
    for j in range(k-1,-1,-1):
        if n==a[i]*a[j]:
            b=a[i]
            e=a[j]
            break
if b==0 and e==0:
    print('-1')
else:
    print(b,e)
