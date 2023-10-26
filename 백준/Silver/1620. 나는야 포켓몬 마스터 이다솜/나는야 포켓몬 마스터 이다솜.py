from sys import stdin
input=stdin.readline
n,m=map(int,input().split())
d={}
for i in range(n):
    d[i+1]=input()[:-1]
dRev={v:k for k,v in d.items()} # key:value -> value:key
for _ in range(m):
    q=input()[:-1]
    try:
        print(d[int(q)])
    except:
        print(dRev[q])