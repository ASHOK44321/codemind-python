N=int(input())
Large=0
while(N!=0):
    Rem=N%10
    N//=10
    if(Rem>Large):
        Large=Rem
print(Large)  