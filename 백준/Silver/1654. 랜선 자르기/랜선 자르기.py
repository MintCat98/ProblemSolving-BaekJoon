from sys import stdin
input=stdin.readline
k,n=map(int,input().split())
l=[]
for _ in range(k):
    l.append(int(input()))
"""
1. 최대길의의 중간점(최대 중간점)으로 잘라봄
2. 최대 중간점으로 자른 길이로 다른 애들 잘라봄 (버려지는 거 감수)
    이때 안 잘리면 0
3. 자른 개수의 합이 n과 같거나 큰지 확인
    맞다면 결과 배열에 해당 길이 추가
4. mid 갱신
    F => right=mid-1
    T => left=mid+1
"""
start=1; end=max(l); ln=len(l); res=[]
while start<=end:
    mid=int((start+end)/2)
    num=0
    for i in range(ln):
        if c:=l[i]//mid:    # non-zero
            num+=c
        else: continue      # zero
    if num>=n:
        res.append(mid)
        start=mid+1
    else: end=mid-1
print(max(res))