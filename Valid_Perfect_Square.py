T=int(input())
for i in range(T):
    n=int(input())
    sq=n**0.5
    for j in range(1,int(sq)+1):
        if(j==sq):
            print("True")
            break
    else:
        print("False")