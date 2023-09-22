from sys import stdin
input=stdin.readline
n=int(input())
l=[]; r=[]
for i in range(n):
    w,h=map(int,input().split())
    l.append((w,h))
for i in range(n):
    # cartesian sets (i,j) 모두 검사
    # 자신 포함
    rank=1
    for j in range(n):
        if l[i][0]<l[j][0] and l[i][1]<l[j][1]:
            rank+=1
    r.append(rank)
print(*r)