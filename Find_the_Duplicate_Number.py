n=int(input())
a=list(map(int,input().split()))
m=0
d=[]
for i in range(n):
    m=0
    for j in range(n):
        if a[i]==a[j]:
            m+=1
    if m>1:
        if a[i] not in d:
            d.append(a[i])
print(*d)
    