import sys
x=int(sys.stdin.readline())
n=int(sys.stdin.readline())
s=0
for i in range(n):
    a,b=map(int,sys.stdin.readline().split())
    s+=a*b
print('Yes') if s==x else print('No')