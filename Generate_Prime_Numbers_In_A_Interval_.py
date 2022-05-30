m=int(input())
n=int(input())
for i in range(m,n+1):
    flag=0
    for j in range(2,i):
        if i%j==0:
            flag=1
            break
    if flag==0 and i!=1:
        print(i)