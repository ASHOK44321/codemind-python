def isPrime(n):
    count=0
    for i in range(1,n+1):
        if n%i==0:
            count+=1
    if count==2:
        return 1
    else:
        return 0

n1=int(input())
n2=int(input())
n3=n1+n2+1
while(n3>0):
    if isPrime(n3)==1:
        print(n3-(n1+n2))
        break
    else:
        n3+=1
