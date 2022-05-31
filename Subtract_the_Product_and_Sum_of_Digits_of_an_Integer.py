n=int(input())
sum=0
pro=1
while(n!=0):
    rem=n%10
    sum=sum+rem
    pro=pro*rem
    n//=10
print(pro-sum)
    