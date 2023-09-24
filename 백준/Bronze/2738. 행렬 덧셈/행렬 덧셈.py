from sys import stdin
input=stdin.readline
m1=[]; m2=[]
a,b=map(int,input().split())
for _ in range(a):
    m1.append(list(map(int,input().split())))
for _ in range(a):
    m2.append(list(map(int,input().split())))
for i in range(a):
    row=[]
    for j in range(b):
        row.append(m1[i][j]+m2[i][j])
    print(*row)