import sys
n=int(sys.stdin.readline())
s=''
for i in range(n):
    print(' '*(n-i-1)+'*'*(i+1))