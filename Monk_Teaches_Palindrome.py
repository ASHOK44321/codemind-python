t=int(input())
while t:
    s=input()
    c=0
    if s==s[::-1]:
        c=1
    if c==1:
        if len(s)%2==0:
            print("YES EVEN")
        else:
            print("YES ODD")
    else:
        print("NO")
    t-=1