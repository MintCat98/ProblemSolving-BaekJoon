from sys import stdin as si
# Recursion은 시간초과, but 피보나치처럼 풀면 풀리긴 함
t=int(si.readline())
for _ in range(t):
    k=int(si.readline())
    n=int(si.readline())
    # (k,n): \sum_{i_k=1}^{n}\sum_{i_{k-1}=1}^{i_k}\cdots\sum_{i_1=1}^{i_2}i_1
    kl=[i for i in range(1,n+1)]
    for a in range(k):
        for b in range(1,n):
            # kl[0]==1 고정
            kl[b]+=kl[b-1]
    print(kl[-1])