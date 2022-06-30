def sum(a):
    k=0
    for i in range(1,a+1):
        if a%i==0:
            k=k+i
    return k
n=list(map(int,input().split(",")))
n.sort()
c=0
for i in n:
    if sum(i) in n:
        print(i,end=" ")
        c+=1
if c==0:
    print("-1")