from sys import stdin as si
from bisect import bisect_left, bisect_right
l=si.readlines()
a=sorted(list(map(int,l[1].split())))
b=list(map(int,l[3].split()))
res=[]
for i in range(len(b)):
    c=bisect_right(a,b[i])-bisect_left(a,b[i])
    res.append(0) if c==0 else res.append(1)
print('\n'.join(map(str,res)))