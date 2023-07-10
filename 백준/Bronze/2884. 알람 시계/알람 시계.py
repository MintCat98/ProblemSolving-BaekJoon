import sys
h,m=map(int,sys.stdin.readline().split())
if m-45<0:
    n=60+(m-45)
    print(23,n) if h-1<0 else print(h-1,n)
else:
    print(h,m-45)