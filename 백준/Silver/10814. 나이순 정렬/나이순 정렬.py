from sys import stdin as si
input=si.readline
n=int(input())
l=[]
for _ in range(n):
    e=input().split()
    e[0]=int(e[0])
    l.append(e)
l.sort(key=lambda x:x[0])
for i in range(n):
    print(*l[i])