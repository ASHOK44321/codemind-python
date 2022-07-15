x,y=map(int,input().split())
l=list(map(int,input().split()))
m=list(map(int,input().split()))
l=set(l)
m=set(m)
c=0
for i in m:
    if i not in l:
        c+=1
for i in l:
    if i not in m:
        c+=1
print(c)
    