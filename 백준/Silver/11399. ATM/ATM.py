from sys import stdin
input=stdin.readline
n=int(input())
l=sorted(list(map(int,input().split())))
sum=0; sub=0
for e in l:
    sub+=e
    sum+=sub
print(sum)