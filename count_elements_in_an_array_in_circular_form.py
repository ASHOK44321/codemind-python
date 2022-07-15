x=int(input())
l=list(map(int,input().split()))
k=list(l)
h=k[0]
j=k[1]
s=l
c=0
s=l.append(h)
s=l.append(j)
for i in range(1,len(l)-1):
    if (l[i-1]%2==0 and l[i+1]%2!=0):
        c+=1
    elif l[i-1]%2!=0 and l[i+1]%2==0:
        c+=1
print(c)