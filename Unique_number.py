n=int(input())
l1=len(str(n))
l2=len(set(str(n)))
if(l1==l2):
    print("Unique Number")
else:
    print("Not Unique Number")
    