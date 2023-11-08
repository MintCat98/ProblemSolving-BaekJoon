from sys import stdin
from collections import deque

input = stdin.readline


def dfs(g, start):
    # Disconnected
    if start not in g:
        return [start]

    visited = []
    s = [start]
    while s:
        # Visit / Small first
        v = s.pop()
        if v not in visited:
            visited.append(v)
        # Find unvisited
        if len(g[v]) == 0:
            continue
        unvisited = sorted(list(set(g[v]) - set(visited)), reverse=True)
        s += unvisited
    return visited


def bfs(g, start):
    # Disconnected
    if start not in g:
        return [start]

    visited = []
    q = deque([start])
    while q:
        # Visit / Small first
        v = q.popleft()
        if v not in visited:
            visited.append(v)
        # Find unvisited
        if len(g[v]) == 0:
            continue
        unvisited = sorted(list(set(g[v]) - set(visited)))
        q.extend(unvisited)
    return visited


n, m, v = map(int, input().split())
# Fill the graph
g = {}
for i in range(m):
    v1, v2 = map(int, input().split())
    if v1 not in g:
        g[v1] = [v2]
    else:
        g[v1].append(v2)
    if v2 not in g:
        g[v2] = [v1]
    else:
        g[v2].append(v1)
print(*dfs(g, v))
print(*bfs(g, v))
