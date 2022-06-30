n=int(input())
a=list(map(int,input().split()))
l=r=m=0
if n%2==0:
    m=-1
    l=r=int(n/2)
else:
    m=n/2
    l=r=int(n/2)
##print(n,l,m,r)
for i in range(n-1,l-1,-1):
    print(a[i],end=" ")
if n%2!=0 or m!=-1:
    print(m,end=" ")
for i in range(0,r):
    print(a[i],end=" ")