# Job Allocation using Branch and Bound

cost = [
    [15, 9, 12, 10],
    [8, 14, 7, 11],
    [13, 6, 10, 9],
    [11, 10, 8, 12]
]

n = 4
minimum_cost = float('inf')
optimal = []

def job_allocation(emp, used_jobs, total_cost, allocation):
    global minimum_cost, optimal

    if emp == n:
        if total_cost < minimum_cost:
            minimum_cost = total_cost
            optimal = allocation[:]
        return

    for job in range(n):
        if job not in used_jobs:
            new_cost = total_cost + cost[emp][job]

            # Branch and Bound
            if new_cost < minimum_cost:
                used_jobs.add(job)
                allocation.append(job)

                job_allocation(
                    emp + 1,
                    used_jobs,
                    new_cost,
                    allocation
                )

                allocation.pop()
                used_jobs.remove(job)

job_allocation(0, set(), 0, [])

print("Optimal Job Allocation")
print("----------------------")
print("Minimum Cost:", minimum_cost)

for i in range(n):
    print("Employee", i + 1,
          "-> Job", optimal[i] + 1)