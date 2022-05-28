n=int(input())
sq=n*n
rev=0
rev2=0
while n!=0:
    rem=n%10
    n//=10
    rev=rev*10+rem
sq2=rev*rev
while sq2!=0:
    rem=sq2%10
    sq2//=10
    rev2=rev2*10+rem
if sq==rev2:
    print("True")
else:
    print("False")