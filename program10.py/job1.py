# Job Allocation using Branch and Bound

n = 4
cost = [
    [9, 2, 7, 8],
    [6, 4, 3, 7],
    [5, 8, 1, 8],
    [7, 6, 9, 4]
]

best_cost = float('inf')
best_assignment = []

def branch_bound(employee, assigned, current_cost, assignment):
    global best_cost, best_assignment

    if employee == n:
        if current_cost < best_cost:
            best_cost = current_cost
            best_assignment = assignment[:]
        return

    for job in range(n):
        if job not in assigned:
            new_cost = current_cost + cost[employee][job]

            if new_cost < best_cost:
                assigned.add(job)
                assignment.append(job)

                branch_bound(
                    employee + 1,
                    assigned,
                    new_cost,
                    assignment
                )

                assignment.pop()
                assigned.remove(job)

branch_bound(0, set(), 0, [])

print("Minimum Cost:", best_cost)
print("Job Allocation:")

for i in range(n):
    print("Employee", i + 1, "-> Job", best_assignment[i] + 1)