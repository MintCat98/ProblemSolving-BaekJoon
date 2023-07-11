import sys
n,x=map(int,sys.stdin.readline().split())
l=list(map(int,sys.stdin.readline().split()))
r=[e for e in l if e<x]
print(*r)