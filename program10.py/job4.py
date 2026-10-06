# Job Allocation Problem using Branch and Bound

cost = [
    [11, 7, 9, 8],
    [6, 10, 5, 9],
    [8, 6, 7, 10],
    [9, 8, 6, 7]
]

n = 4
best = float('inf')
result = []

def branch(employee, selected, current, allocation):
    global best, result

    if employee == n:
        if current < best:
            best = current
            result = allocation[:]
        return

    for job in range(n):
        if job not in selected:
            cost_now = current + cost[employee][job]

            if cost_now < best:
                selected.add(job)
                allocation.append(job)

                branch(employee + 1,
                       selected,
                       cost_now,
                       allocation)

                allocation.pop()
                selected.remove(job)

branch(0, set(), 0, [])

print("Minimum Cost:", best)
print("\nEmployee - Job")

for i in range(n):
    print("Employee", i + 1,
          " - Job", result[i] + 1)