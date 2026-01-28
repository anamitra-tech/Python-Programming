def knapsack_01(W, weights, profits):
    n = len(weights)

    # dp[w] = maximum profit achievable with capacity w
    dp = [0] * (W + 1)

    # process each item once
    for i in range(n):
        wt = weights[i]
        val = profits[i]

        # IMPORTANT: backward loop
        for w in range(W, wt - 1, -1):
            dp[w] = max(dp[w], dp[w - wt] + val)

    return dp[W]
