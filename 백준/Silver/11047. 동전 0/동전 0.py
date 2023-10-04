from sys import stdin
input=stdin.readline
n,k=map(int,input().split())
ps=[]
for _ in range(n): ps.append(int(input()))
ct=0
for i in range(len(ps)-1,-1,-1):
    ct+=k//ps[i]    # 개수 갱신
    k%=ps[i]        # 남은 금액 갱신
print(ct)