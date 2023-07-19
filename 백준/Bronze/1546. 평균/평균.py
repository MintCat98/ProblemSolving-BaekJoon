from sys import stdin as si
n=int(si.readline())
l=list(map(int,si.readline().split()))
print(sum(l)/(max(l)*n)*100)