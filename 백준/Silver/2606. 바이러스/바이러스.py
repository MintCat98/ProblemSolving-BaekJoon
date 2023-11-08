from sys import stdin


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


input = stdin.readline
n = int(input())
m = int(input())
v_dfs = [False] * (n + 1)
g = [[] for _ in range(n + 1)]
for _ in range(m):
    v1, v2 = map(int, input().split())
    g[v1].append(v2)
    g[v2].append(v1)

r_dfs = []
dfs(1)
print(len(r_dfs) - 1)
