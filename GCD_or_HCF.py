n,m=[int(x) for x in input().split()]
if n>m:
    smaller=m
else:
    smaller=n
for i in range(1,smaller+1):
    if n%i==0 and m%i==0:
        hcf=i
print(hcf)