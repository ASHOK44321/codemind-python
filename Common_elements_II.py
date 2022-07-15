x,y=map(int,input().split())
l=list(map(int,input().split()))
m=list(map(int,input().split()))
for i in m:
    l.append(i)
for i in l:
    k=l.count(i)
    if(k==1):
        print(i,end=" ")