I,r,k=[int(x) for x in input().split()]
count=0
for i in range(I,r+1):
    if i%k==0:
        count+=1
print(count)