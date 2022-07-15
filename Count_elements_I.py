x,y=map(int,input().split())
l=list(map(int,input().split()))
m=list(map(int,input().split()))
k=set(l)
n=set(m)
c=0
for i in k:
    if i in n:
        c+=1
print(c)