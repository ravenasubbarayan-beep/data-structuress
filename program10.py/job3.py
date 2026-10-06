# Branch and Bound Job Allocation

cost = [
    [12, 4, 8],
    [7, 9, 5],
    [6, 10, 7]
]

n = 3
minimum = float('inf')
answer = []

def allocate(worker, used, total, jobs):
    global minimum, answer

    if worker == n:
        if total < minimum:
            minimum = total
            answer = jobs.copy()
        return

    for task in range(n):
        if task not in used:
            new_total = total + cost[worker][task]

            if new_total < minimum:
                used.add(task)
                jobs.append(task)

                allocate(worker + 1, used, new_total, jobs)

                jobs.pop()
                used.remove(task)

allocate(0, set(), 0, [])

print("Minimum Cost =", minimum)
print("Optimal Allocation:")

for worker in range(n):
    print("Employee", worker + 1,
          "-> Task", answer[worker] + 1)