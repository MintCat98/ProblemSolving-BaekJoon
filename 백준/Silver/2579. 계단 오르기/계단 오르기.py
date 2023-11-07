# DP: Bottom-up
from sys import stdin

n = int(stdin.readline())
s = []
for _ in range(n):
    s.append(int(stdin.readline()))
# s = list(map(int, stdin.readlines()))
if n <= 2:
    print(sum(s))
else:
    dp = [0] * n
    dp[0] = s[0]
    dp[1] = s[0] + s[1]
    for i in range(2, n):
        dp[i] = max((s[i] + s[i - 1] + dp[i - 3]), (s[i] + dp[i - 2]))
    print(dp[-1])
