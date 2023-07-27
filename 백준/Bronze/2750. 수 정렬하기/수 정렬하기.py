from sys import stdin as si
input=si.readlines
l=list(map(int,input()[1:]))
l.sort()
for i in range(len(l)): print(l[i])