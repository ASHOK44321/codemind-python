n=int(input())
a=list(map(int,input().split()))
k=n
t=i=0
while n:
    t=(t*10)+a[i]
    i+=1
    n-=1
e=t+1
h=p=0
d=[]
while(e):
    h=e%10
    d.append(h)
    e=e//10
for i in range(len(d)-1,-1,-1):
    print(d[i],end=" ")