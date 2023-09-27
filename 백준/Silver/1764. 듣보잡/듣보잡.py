from sys import stdin
input=stdin.readline
n,m=map(int,input().split())
dd=set(); bd=set()
for _ in range(n):
    dd.add(input().rstrip())
for _ in range(m):
    bd.add(input().rstrip())
db=sorted(dd.intersection(bd))
print(len(db))
print('\n'.join(db))