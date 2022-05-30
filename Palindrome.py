n=int(input())
x=n
rev=0
while x>0:
    rem=x%10
    rev=rev*10+rem
    x//=10
if n==rev:
    print("True")
else:
    print("False")
    