from sys import stdin
from collections import deque


def dfs(start):
    v_dfs[start] = True
    r_dfs.append(start)
    stack = sorted(g[start], reverse=True)
    while stack:
        visit = stack.pop()
        if not v_dfs[visit]:
            v_dfs[visit] = True
            r_dfs.append(visit)
            stack += sorted(g[visit], reverse=True)


def bfs(start):
    v_bfs[start] = True
    r_bfs.append(start)
    queue = deque(sorted(g[start]))
    while queue:
        visit = queue.popleft()
        if not v_bfs[visit]:
            v_bfs[visit] = True
            r_bfs.append(visit)
            queue.extend(sorted(g[visit]))


input = stdin.readline
n, m, v = map(int, input().split())
# 공간 미리 확보
v_dfs = [False] * (n + 1)
v_bfs = [False] * (n + 1)
g = [[] for _ in range(n + 1)]
for _ in range(m):
    v1, v2 = map(int, input().split())
    g[v1].append(v2)
    g[v2].append(v1)

r_dfs = []
r_bfs = []
dfs(v)
bfs(v)
print(*r_dfs)
print(*r_bfs)
