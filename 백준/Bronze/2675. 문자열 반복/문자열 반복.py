import sys
t=int(sys.stdin.readline())
for i in range(t):
    r,s=sys.stdin.readline().split()
    r=int(r)
    a=''
    for j in range(len(s)):
        a+=s[j]*r
    print(a)