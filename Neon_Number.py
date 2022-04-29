n = int(input())
sqr =n*n
sumOfDigit = 0
while sqr>0:
    sumOfDigit =sumOfDigit + sqr%10
    sqr = sqr//10

if (n == sumOfDigit):
    print("Neon Number")
else:
    print("Not Neon Number")