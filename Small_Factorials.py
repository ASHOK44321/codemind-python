T=int(input())
for i in range(T):
    N=int(input())
    fact=1
    for j in range(1,N+1):
        fact*=j
    print(fact)