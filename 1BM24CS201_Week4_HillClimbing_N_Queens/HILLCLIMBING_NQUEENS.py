def calculate_cost(state):
    """Calculate number of attacking queen pairs."""
    cost = 0
    n = len(state)

    for i in range(n):
        for j in range(i + 1, n):

            # Same row
            if state[i] == state[j]:
                cost += 1

            # Same diagonal
            elif abs(state[i] - state[j]) == abs(i - j):
                cost += 1

    return cost


def generate_neighbors(state):
    """Generate all states by swapping two queens."""
    neighbors = []

    n = len(state)

    for i in range(n):
        for j in range(i + 1, n):

            new_state = state.copy()

            # Swap two queens
            new_state[i], new_state[j] = new_state[j], new_state[i]

            cost = calculate_cost(new_state)

            neighbors.append((new_state, cost, i, j))

    return neighbors


def print_matrix(state):
    """Display the state as an N x N matrix."""

    n = len(state)

    for row in range(n):
        for col in range(n):

            if state[row] == col:
                print("Q", end=" ")
            else:
                print("0", end=" ")

        print()


def hill_climbing(initial_state):

    current = initial_state.copy()
    current_cost = calculate_cost(current)

    # Store optimal/selected solution path
    path = [current.copy()]

    print("\n===================================")
    print("        INITIAL STATE")
    print("===================================")

    print("State:", current)
    print("Cost :", current_cost)

    print("\nMatrix:")
    print_matrix(current)

    while True:

        neighbors = generate_neighbors(current)

        print("\n-----------------------------------")
        print("Neighbours")
        print("-----------------------------------")

        for state, cost, i, j in neighbors:

            print(
                f"Swap (x{i}, x{j}) -> "
                f"{state}, Cost = {cost}"
            )

        # Find minimum-cost neighbour
        best_neighbor = min(
            neighbors,
            key=lambda x: (x[1], x[2], x[3])
        )

        best_state, best_cost, i, j = best_neighbor

        # If no improvement
        if best_cost >= current_cost:

            print("\nNo better neighbour found.")
            print("Hill climbing terminates.")

            break

        print(
            f"\nSelected move: Swap (x{i}, x{j})"
        )

        current = best_state
        current_cost = best_cost

        # Add state to path
        path.append(current.copy())

        print("\nNew State:", current)
        print("Cost     :", current_cost)

        print("\nMatrix:")
        print_matrix(current)

        # Goal reached
        if current_cost == 0:

            print("\nSolution found!")

            break

    # --------------------------------
    # Display Solution Path
    # --------------------------------

    print("\n\n===================================")
    print("        SOLUTION PATH")
    print("===================================")

    for step, state in enumerate(path):

        cost = calculate_cost(state)

        print(f"\nStep {step}")
        print("State:", state)
        print("Cost :", cost)

        print("Matrix:")

        print_matrix(state)

    print("\n===================================")
    print("           FINAL RESULT")
    print("===================================")

    print("Final State:", current)
    print("Final Cost :", current_cost)

    if current_cost == 0:
        print("Status     : Solution Found")
    else:
        print("Status     : Local Minimum")


# --------------------------------
# Dynamic Input
# --------------------------------

n = int(input("Enter number of queens: "))

print(f"Enter {n} values representing the queen positions.")
print("Example for 4 queens: 3 1 2 0")

initial_state = list(
    map(int, input("Enter initial state: ").split())
)

if len(initial_state) != n:

    print(
        "Error: Number of values must match "
        "number of queens."
    )

elif sorted(initial_state) != list(range(n)):

    print(
        "Error: Enter a permutation of 0 to",
        n - 1
    )

else:

    hill_climbing(initial_state)