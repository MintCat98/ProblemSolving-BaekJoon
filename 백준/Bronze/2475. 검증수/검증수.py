import sys
l=list(map(int,sys.stdin.readline().split()))
r=0
for e in l:
    r+=e**2
print(r%10)