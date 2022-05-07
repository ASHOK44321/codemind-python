a=int(input())
f=0
for i in range(1,a):
    if i*i==a:
        f=1
        break
if f==1:
    print("True")
else:
    print("False")