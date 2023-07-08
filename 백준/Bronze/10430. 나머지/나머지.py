import sys
A,B,C=map(int,sys.stdin.readline().split())
l=[(A+B)%C, ((A%C)+(B%C))%C, (A*B)%C, ((A%C)*(B%C))%C]
for i in range(len(l)):
    print(l[i])