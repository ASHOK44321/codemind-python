n=int(input())
while n>=10:
    sum=0
    while n!=0:
        rem=n%10
        n//=10 
        sum+=rem**2
    n=sum
if n==1 or n==7:
    print("True")
else:
    print("False")