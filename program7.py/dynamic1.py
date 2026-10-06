# Fractional Knapsack using Greedy Algorithm

n = int(input("Enter number of items: "))

items = []

for i in range(n):
    weight = float(input(f"Enter weight of item {i+1}: "))
    profit = float(input(f"Enter profit of item {i+1}: "))
    ratio = profit / weight
    items.append((weight, profit, ratio))

capacity = float(input("Enter knapsack capacity: "))

# Sort according to profit/weight ratio
items.sort(key=lambda x: x[2], reverse=True)

total_profit = 0

for weight, profit, ratio in items:
    if capacity >= weight:
        capacity -= weight
        total_profit += profit
    else:
        fraction = capacity / weight
        total_profit += profit * fraction
        break

print("Maximum Profit =", total_profit)