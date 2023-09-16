from sys import stdin as si
from collections import deque
t=int(si.readline())
for _ in range(t):
    m,n=map(int,si.readline().split())
    l=list(map(int,si.readline().split()))
    q0=deque(); q1=deque()
    for i in range(m):
        # (loc, val)
        q0.append((i,l[i]))
    # Priority 기준 정렬
    ct=0
    while ct!=m:
        e=q0.popleft()
        mx=max(l)
        if e[1] == mx:
            q1.append(e); l.remove(mx); ct+=1
        elif e[1] < mx:
            q0.append(e)
    # 정답 찾기
    for i in range(m):
        res=q1.popleft()
        if res[0]==n: print(i+1); break