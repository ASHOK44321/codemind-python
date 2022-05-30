n=int(input())
sum=0
x=n
order=len(str(n))
while x>0:
    rem=x%10
    sum=sum+rem**order
    x//=10
    order-=1
if sum==n:
    print("True")
else:
    print("False")