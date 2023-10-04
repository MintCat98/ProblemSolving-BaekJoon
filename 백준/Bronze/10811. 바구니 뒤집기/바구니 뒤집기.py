from sys import stdin
input = stdin.readline
n, m = map(int, input().split())
bs = [i for i in range(1, n+1)]
for _ in range(m):
    a, b = map(int, input().split())
    a -= 1
    b -= 1
    avg = (a+b)//2
    for i in range(a, avg+1):
        bs[i], bs[b-i+a] = bs[b-i+a], bs[i]
print(*bs)
