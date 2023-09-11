from sys import stdin as si
from collections import deque
n, k = map(int, si.readline().split())
q = deque()
l = []
for i in range(1, n+1):
    q.append(i)
for _ in range(n):
    for _ in range(k-1):
        q.append(q.popleft())
    l.append(q.popleft())
print('<'+', '.join(map(str, l))+'>')
