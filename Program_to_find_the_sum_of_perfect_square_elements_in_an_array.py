def per(a):
    if int(a**0.5)==a**0.5:
        return 1
    return 0
n=int(input())
a=list(map(int,input().split()))
s=0
for i in a:
    if per(i)==1:
        s=s+i
print(s)