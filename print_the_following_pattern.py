N=int(input())
for i in range(1,N+1):
    for j in range(i,N+1):
        print(chr(65+N-i),end=" ")
    print()