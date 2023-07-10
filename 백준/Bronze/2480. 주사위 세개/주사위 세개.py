import sys
a,b,c=map(int,sys.stdin.readline().split())
l=sorted([a,b,c])
s=set(l)
if len(s)==1:
    print(10000+a*1000)
elif len(s)==2:
    print(1000+l[1]*100)
else:
    print(l[2]*100)