from sys import stdin as si
l=[]
for _ in range(int(si.readline())):
    x,y=map(int,si.readline().split())
    l.append((x,y))
l.sort()
for i in range(len(l)):
    print(f'{l[i][0]} {l[i][1]}')