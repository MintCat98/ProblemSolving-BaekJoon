from sys import stdin as si
n=int(si.readline())
l=list(map(int,si.readline().split()))
m=max(l)
for i in range(n):
    l[i]=l[i]/m*100
print(sum(l)/n)