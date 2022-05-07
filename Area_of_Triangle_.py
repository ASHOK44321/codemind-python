import math
m,n,o=map(int,input().split())
r=(m+n+o)/2
a=r*(r-m)*(r-n)*(r-o)
area=math.pow(a,0.5)
print("{:.2f}".format(area))