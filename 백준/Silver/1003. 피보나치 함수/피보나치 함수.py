from sys import stdin
input=stdin.readline
def fibDP(n,list):
    list[0]=[1,0]; list[1]=[0,1]
    for i in range(2,n+1):
        list[i]=[(list[i-1][0]+list[i-2][0]),(list[i-1][1]+list[i-2][1])]

t=int(input())
fibResult=[0]*41     # 0~40
for _ in range(t):
    n=int(input())
    fibDP(n,fibResult)
    print(*fibResult[n])