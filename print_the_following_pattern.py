N=int(input())
for i in range(1,N+1):
    for j in range(1,N-1):
        print(j,end="")
    for k in range(N-3,0,-1):
        print(k,end="")
    print()