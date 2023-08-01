n=int(input())
for i in range(1,n+1):
    s=' '*(n-i)+'*'*(2*i-1)
    print(s)
for i in range(n-1,0,-1):
    s=' '*(n-i)+'*'*(2*i-1)
    print(s)