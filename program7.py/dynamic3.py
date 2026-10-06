# Greedy Fractional Knapsack

items = [
    ("Item 1", 10, 60),
    ("Item 2", 20, 100),
    ("Item 3", 30, 120),
    ("Item 4", 15, 90)
]

capacity = 50

items.sort(key=lambda x: x[2] / x[1], reverse=True)

profit = 0

print("Selected Items:")

for name, weight, value in items:
    if capacity >= weight:
        capacity -= weight
        profit += value
        print(name, "- Full")
    else:
        fraction = capacity / weight
        profit += value * fraction
        print(name, "-", round(fraction * 100, 2), "%")
        break

print("Maximum Profit =", round(profit, 2))