import math
n=int(input())
s=math.sqrt(n)
for i in range(n):
    if(s==i):
        print("True")
        break
else:
    print("False")
