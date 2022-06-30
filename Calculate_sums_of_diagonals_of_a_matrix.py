n = int(input().strip())
a = [[0]*n for _ in range(n)]
for i in range(n):
    a[i] = [int(j) for j in input().strip().split(" ")]
s1=0
s2=0
for i in range(n):
    for j in range(n):
        if i==j:
            s1=s1+a[i][j]
for i in range(n):
    for j in range(n):
        if (n-i-1)==j:
            s2=s2+a[i][j]
print("Principal Diagonal:%d"%s1)
print("Secondary Diagonal:%d"%s2)