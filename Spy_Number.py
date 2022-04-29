N=int(input())
sum=0
product=1
N1=N
while(N>0):
    
    d=N%10
    sum=sum+d
    product=product*d
    N=N//10
if(sum==product):
    print("Spy Number".format(N1))
else:
    print("Not Spy Number".format(N1))

