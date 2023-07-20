from sys import stdin as si
n,k=map(int,si.readline().split())
c,m=1,1
for i in range(k):
    c*=n-i
    m*=k-i
print(int(c/m))