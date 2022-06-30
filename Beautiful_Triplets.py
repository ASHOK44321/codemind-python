n=int(input())
a=list(map(int,input().split()))
a.sort()
d=[]
for i in a:
    if i not in d:
        d.append(i)
c=0
k=1
for i in d:
    ##print(d)
    for j in range(k,len(d)):
        d[j]-=i
    k+=1
for i in range(len(d)):
    c=0
    for j in range(len(a)):
       a[j]=a[j]-d[i]
       if a[j]>=0:
           c+=1
    print(c)
    