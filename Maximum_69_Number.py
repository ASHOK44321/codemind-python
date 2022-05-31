n=int(input())
s=str(n)
l=list(s)
for i in range(len(s)):
    if l[i]=='6':
        l[i]='9'
        break
n=''.join(l)
print(int(n))