n=int(input())
sq=n*n
order=len(str(n))
rem=sq%(10**order)
if(rem==n):
    print("Automorphic Number")
else:
    print("Not an Automorphic Number")