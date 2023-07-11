import sys
n,m=map(int,sys.stdin.readline().split())
l=[i for i in range(1,n+1)]
for i in range(m):
    a,b=map(int,sys.stdin.readline().split())
    a-=1;b-=1
    l[a],l[b]=l[b],l[a]
print(*l)