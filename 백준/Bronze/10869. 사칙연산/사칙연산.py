import sys
a,b=map(int,sys.stdin.readline().split())
l=[a+b,a-b,a*b,a//b,a%b]
for i in range(len(l)):
    print(l[i])