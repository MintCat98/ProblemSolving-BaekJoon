from sys import stdin
import heapq
# 4사5입 구현
def round2(n):
    return int(n)+(1 if n-int(n)>=0.5 else 0)
input=stdin.readline
n=int(input())
if n==0: print(0)
else:
    h=[]; r=[]
    # Heap-sort
    for _ in range(n):
        heapq.heappush(h,int(input()))
    for i in range(n):
        r.append(heapq.heappop(h))
    rd=round2(n*0.15)
    print(round2(sum(r[rd:n-rd])/(n-2*rd)))