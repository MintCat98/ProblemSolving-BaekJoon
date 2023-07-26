from sys import stdin as si
l=list(range(1,31))
for _ in range(28):
    l.remove(int(si.readline()))
print('\n'.join(map(str,sorted(l))))