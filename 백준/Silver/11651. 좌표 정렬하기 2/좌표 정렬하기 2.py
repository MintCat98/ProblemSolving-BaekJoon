from sys import stdin
input=stdin.readline
n=int(input())
l=[]
for _ in range(n):
    x,y=map(int,input().split())
    l.append((x,y))
l.sort(key=lambda x:(x[1],x[0]))
for i in range(n):
    print(*l[i])