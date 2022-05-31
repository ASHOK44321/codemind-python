n=int(input())
for i in range(n):
    if(n==i*(i+1)):
        print("YES")
        break
else:
    print("NO")