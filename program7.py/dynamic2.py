# 0/1 Knapsack using Dynamic Programming

n = int(input("Enter number of items: "))

weights = []
profits = []

for i in range(n):
    weights.append(int(input(f"Enter weight of item {i+1}: ")))
    profits.append(int(input(f"Enter profit of item {i+1}: ")))

capacity = int(input("Enter knapsack capacity: "))

dp = [[0 for _ in range(capacity + 1)]
      for _ in range(n + 1)]

for i in range(1, n + 1):
    for w in range(1, capacity + 1):
        if weights[i - 1] <= w:
            dp[i][w] = max(
                profits[i - 1] + dp[i - 1][w - weights[i - 1]],
                dp[i - 1][w]
            )
        else:
            dp[i][w] = dp[i - 1][w]

print("Maximum Profit =", dp[n][capacity])