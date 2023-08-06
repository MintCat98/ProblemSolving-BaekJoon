from sys import stdin as si
input=si.readline
n,m=map(int,input().split())
l=list(map(int,input().split()))
save=0
for i in range(n):
    a=l[i]
    for j in range(n):
        if j==i: continue
        b=l[j]
        for k in range(n):
            if k==i or k==j: continue
            c=l[k]
            s=a+b+c
            if s>m: continue
            elif s==m: save=s; break
            else:
                if s>save: save=s
print(save)