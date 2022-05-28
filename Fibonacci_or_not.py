n = int(input())
r1=(5*(n**2))+4
r2=(5*(n**2))-4
a=int(r1**0.5)
b=int(r2**0.5)
if a*a==r1 or b*b==r2:
    print("True")
else:
    print("False")