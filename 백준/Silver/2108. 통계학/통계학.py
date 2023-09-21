from sys import stdin
import heapq
def round2(n):
    return int(n)+(1 if n-int(n)>=0.5 else 0)
input=stdin.readline
n=int(input())
# Heap-sort
h=[]; r=[]
for _ in range(n):
    heapq.heappush(h,int(input()))
for i in range(n):
    r.append(heapq.heappop(h))
# Cal Avg
s=sum(r)
if s>=0: a=round2(s/n)
else: a=-round2(-s/n)
# Cal Mode
m=0; d={e: 0 for e in r}; k=d.keys()
for e in r:
    if e in k: d[e]+=1
c=sorted(d.items(), key=lambda x: x[1])
ms=[c[-1]]
for i in range(len(c)-2,-1,-1):
    if c[i][1] == c[-1][1]:
        ms.append(c[i])
    else: break
if len(ms)>=2: m=ms[-2][0]
else: m=ms[0][0]
print(f'{a}\n{r[int(n*0.5)]}\n{m}\n{r[-1]-r[0]}')