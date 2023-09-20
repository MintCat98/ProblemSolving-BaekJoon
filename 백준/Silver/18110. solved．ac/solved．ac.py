from sys import stdin
import heapq
# 4사5입 구현
def round2(n):
    return int(n)+(1 if n-int(n)>=0.5 else 0)
input=stdin.readline
n=int(input())
if n==0: print(0)
else:
    h=[]; r=[]; s=0
    for _ in range(n):
        heapq.heappush(h,int(input()))
    # Heap-sort
    for i in range(n):
        r.append(heapq.heappop(h))
    rd=round2(n*0.15)
    for e in r[rd:n-rd]:
        s+=e
    print(round2(s/(n-2*rd)))