# DP: Bottom-up (Known Base Cases)
def solve(n):
    dp={1:0,2:1,3:1}
    for i in range(4,n+1):
        # 1 뺀 값의 횟수로 초기화
        dp[i]=dp[i-1]+1
        # Compare
        # 2로 나눠떨어지면 초기화값과 2로 나눠진 값의 횟수+1 중 작은 값
        if i%2==0: dp[i]=min(dp[i],dp[i//2]+1)
        # 3으로 나눠떨어지면 현재값과 3으로 나눠진 값의 횟수+1 중 작은 값
        if i%3==0: dp[i]=min(dp[i],dp[i//3]+1)
    return dp[n]

print(solve(int(input())))