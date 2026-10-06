# 0/1 Knapsack using Function

def knapsack(weights, profits, capacity):
    n = len(weights)

    dp = [0] * (capacity + 1)

    for i in range(n):
        for w in range(capacity, weights[i] - 1, -1):
            dp[w] = max(dp[w],
                         profits[i] + dp[w - weights[i]])

    return dp[capacity]


weights = [2, 3, 4, 5]
profits = [3, 4, 5, 6]
capacity = 5

result = knapsack(weights, profits, capacity)

print("Weights:", weights)
print("Profits:", profits)
print("Capacity:", capacity)
print("Maximum Profit:", result)