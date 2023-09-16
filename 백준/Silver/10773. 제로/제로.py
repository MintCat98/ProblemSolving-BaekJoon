from sys import stdin as si
l=list(map(int,si.readlines()[1:]))
s=[]
for e in l:
    s.append(e) if e!=0 else s.pop()
print(sum(s))