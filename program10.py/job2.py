# Job Allocation using Branch and Bound

cost = [
    [10, 5, 8, 9],
    [7, 6, 4, 8],
    [9, 7, 5, 6],
    [6, 8, 7, 5]
]

n = len(cost)
best_cost = float('inf')
best = []

def solve(emp, used, total, allocation):
    global best_cost, best

    if emp == n:
        if total < best_cost:
            best_cost = total
            best = allocation[:]
        return

    for job in range(n):
        if job not in used:
            new_total = total + cost[emp][job]

            if new_total < best_cost:
                used.add(job)
                allocation.append(job)

                solve(emp + 1, used, new_total, allocation)

                allocation.pop()
                used.remove(job)

solve(0, set(), 0, [])

print("Minimum Allocation Cost:", best_cost)

for i, job in enumerate(best):
    print("Employee", i + 1, "assigned to Job", job + 1)