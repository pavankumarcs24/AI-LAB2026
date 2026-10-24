
import heapq

def heuristic(state, goal):
    distance = 0

    for i in range(9):
        tile = state[i]

        if tile != 0:
            j = goal.index(tile)
            distance += abs(i // 3 - j // 3)
            distance += abs(i % 3 - j % 3)

    return distance

def get_neighbors(state):
    neighbors = []
    blank = state.index(0)

    for move in [-3, 3, -1, 1]:
        pos = blank + move

        if pos < 0 or pos >= 9:
            continue

        if abs(move) == 1 and blank // 3 != pos // 3:
            continue

        board = list(state)
        board[blank], board[pos] = board[pos], board[blank]
        neighbors.append(tuple(board))

    return neighbors

def astar(start, goal):
    pq = [(heuristic(start, goal), 0, start)]
    best_g = {start: 0}
    parent = {}

    while pq:
        f, g, state = heapq.heappop(pq)

        if g != best_g.get(state):
            continue

        if state == goal:
            path = []

            while state in parent:
                path.append(state)
                state = parent[state]

            path.append(state)
            path.reverse()

            print("\nSolution found!")
            print("Total moves:", len(path) - 1)

            for step, board in enumerate(path):
                print("\nStep", step)

                for i in range(0, 9, 3):
                    print(board[i:i + 3])

                h = heuristic(board, goal)
                g = step
                print("g =", g, "h =", h, "f =", g + h)

            return

        for nxt in get_neighbors(state):
            new_g = g + 1

            if new_g < best_g.get(nxt, float('inf')):
                best_g[nxt] = new_g
                parent[nxt] = state
                h = heuristic(nxt, goal)

                heapq.heappush(pq, (new_g + h, new_g, nxt))

    print("No solution found.")

print("Enter initial matrix (use 0 for blank):")
start = []

for _ in range(3):
    start.extend(map(int, input().split()))

print("Enter goal matrix:")
goal = []

for _ in range(3):
    goal.extend(map(int, input().split()))

if sorted(start) != list(range(9)) or sorted(goal) != list(range(9)):
    print("Invalid input! Use each number from 0 to 8 exactly once.")
else:
    astar(tuple(start), tuple(goal))
