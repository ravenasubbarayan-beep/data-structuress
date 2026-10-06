from collections import deque

graph = {
    0: [1, 2],
    1: [0, 3],
    2: [0, 4],
    3: [1, 4],
    4: [2, 3]
}

def bfs(start):
    visited = set([start])
    queue = deque([start])

    print("BFS Traversal:", end=" ")

    while queue:
        v = queue.popleft()
        print(v, end=" ")

        for x in graph[v]:
            if x not in visited:
                visited.add(x)
                queue.append(x)

def dfs(start):
    visited = set()

    def visit(v):
        visited.add(v)
        print(v, end=" ")

        for x in graph[v]:
            if x not in visited:
                visit(x)

    print("DFS Traversal:", end=" ")
    visit(start)


while True:
    print("\n\n1. Display Graph")
    print("2. BFS")
    print("3. DFS")
    print("4. Exit")

    choice = int(input("Enter your choice: "))

    if choice == 1:
        print("Graph:")
        for v in graph:
            print(v, "->", graph[v])

    elif choice == 2:
        start = int(input("Enter starting vertex: "))
        bfs(start)

    elif choice == 3:
        start = int(input("Enter starting vertex: "))
        dfs(start)

    elif choice == 4:
        print("Program ended.")
        break

    else:
        print("Invalid choice!")