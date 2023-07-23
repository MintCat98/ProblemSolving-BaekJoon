from sys import stdin as si
m,n=map(int,si.readline().split())
c=0
for i in range(m,n+1):
    if i==1: continue   # 예외
    for j in range(2,int(i**0.5)+1):    # 에라토스테네스의 체
        if i%j==0: break
    else:   # for문 모두 통과할 때만 출력
        print(i)