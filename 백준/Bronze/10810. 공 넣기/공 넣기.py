import sys
n,m=map(int,sys.stdin.readline().split())
d={}
for i in range(n):
    d[i+1]=0
for x in range(m):
    i,j,k=map(int,sys.stdin.readline().split())
    for y in range(i,j+1):
        d[y]=k
print(*d.values())