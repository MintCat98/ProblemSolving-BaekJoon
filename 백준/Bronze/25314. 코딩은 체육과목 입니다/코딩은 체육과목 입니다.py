import sys
n=int(sys.stdin.readline())
a,b=n//4,n%4
s=''
for i in range(a):
    s+='long '
if b!=0:
    s+='long '
print(f'{s}int')