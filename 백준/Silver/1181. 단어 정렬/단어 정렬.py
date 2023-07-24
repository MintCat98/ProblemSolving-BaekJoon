from sys import stdin as si
l=set()
for _ in range(int(si.readline())):
    l.add(si.readline()[:-1])
l=list(l)
l.sort(); l.sort(key=lambda s:len(s))
print('\n'.join(l))