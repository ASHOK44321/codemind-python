a,b=[int(x) for x in input().split()]
if(a>b):
    smaller=b
else:
    smaller=a
for i in range(1,smaller+1):
    if a%i==0 and b%i==0:
        hcf=i
lcm=(a*b)//hcf
print(lcm)