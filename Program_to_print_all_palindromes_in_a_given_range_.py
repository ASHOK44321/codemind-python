m=int(input())
n=int(input())
for j in range(m,n+1):
    rev=0
    i=j
    while(i!=0):
        rem=i%10
        rev=(rev*10)+rem
        i//=10
    if(j==rev):
        print(j,end=" ")