def func(n):
    dp = [0 for i in range(n+1)]
    dp[0] = 1
    dp[1] = 1
    dp[2] = 2
    for i in range(3,n+1):
        dp[i] = dp[i-1] + dp[i-2] + dp[i-3]
    return dp[n]

n = int(input('enter no of stairs'))
print(func(n))