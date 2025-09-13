def coinChange(c, a):
    dp = [a + 1] * (a + 1)
    dp[0] = 0
    for i in range(1, a + 1):
        for x in c:
            if i - x >= 0:
                dp[i] = min(dp[i], 1 + dp[i - x])
    return dp[a] if dp[a] != a + 1 else -1

tests = [
    ([1, 2, 5], 11),
    ([2], 3),
    ([1], 0)
]

for c, a in tests:
    print(coinChange(c, a))
