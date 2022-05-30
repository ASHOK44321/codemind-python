N=int(input())
fcount=0
for i in range(1,N+1):
    if N%i==0:
        count=0
        for j in range(1,i+1):
            if i%j==0:
                count+=1
        if count!=2:
            fcount+=1
print(fcount) 
                