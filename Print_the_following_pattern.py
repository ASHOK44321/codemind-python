N=int(input())
for i in range(1,N+1):
    for j in range(i,N):
        print(end=" ")
    for k in range(1,i+1):
        print(chr(64+k),end="")
    for l in range(i-1,0,-1):
        print(chr(64+l),end="")
    print()