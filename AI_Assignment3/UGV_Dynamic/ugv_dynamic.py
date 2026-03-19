import random
import heapq
import time
import matplotlib.pyplot as plt
import numpy as np
from matplotlib.colors import ListedColormap
import matplotlib.patches as mpatches

# Generate Grid
def generate_grid(size, density):
    return [[1 if random.random() < density else 0 for _ in range(size)] for _ in range(size)]


# A* Algorithm
def astar(grid, start, goal):
    rows, cols = len(grid), len(grid[0])

    def heuristic(a, b):
        return abs(a[0] - b[0]) + abs(a[1] - b[1])

    pq = [(0, start)]
    g_cost = {start: 0}
    parent = {start: None}

    nodes_explored = 0
    directions = [(0,1),(1,0),(-1,0),(0,-1)]

    while pq:
        _, current = heapq.heappop(pq)
        nodes_explored += 1

        if current == goal:
            return parent, nodes_explored

        for d in directions:
            nx, ny = current[0] + d[0], current[1] + d[1]

            if 0 <= nx < rows and 0 <= ny < cols and grid[nx][ny] == 0:
                new_cost = g_cost[current] + 1

                if (nx, ny) not in g_cost or new_cost < g_cost[(nx, ny)]:
                    g_cost[(nx, ny)] = new_cost
                    priority = new_cost + heuristic((nx, ny), goal)
                    heapq.heappush(pq, (priority, (nx, ny)))
                    parent[(nx, ny)] = current

    return None, nodes_explored


# Reconstruct Path
def get_path(parent, goal):
    if parent is None or goal not in parent:
        return []

    path = []
    while goal:
        path.append(goal)
        goal = parent.get(goal)
    return path[::-1]


# Add Dynamic Obstacle
def add_dynamic_obstacle(grid, current, goal, probability=0.3):
    size = len(grid)

    if random.random() < probability:
        while True:
            x = random.randint(0, size-1)
            y = random.randint(0, size-1)

            if (x, y) != current and (x, y) != goal:
                grid[x][y] = 1
                break


# Visualization (ANIMATED 🔥)
def visualize_grid(grid, path, current, goal):
    grid_np = np.array(grid)

    for (i, j) in path:
        grid_np[i][j] = 2  # path

    grid_np[current[0]][current[1]] = 3  # robot
    grid_np[goal[0]][goal[1]] = 4

    cmap = ListedColormap([
        "white",   # free
        "black",   # obstacle
        "yellow",  # path
        "blue",    # robot
        "red"      # goal
    ])

    plt.imshow(grid_np, cmap=cmap)

    # Legend
    legend_elements = [
        mpatches.Patch(color='white', label='Free Space'),
        mpatches.Patch(color='black', label='Obstacle'),
        mpatches.Patch(color='yellow', label='Path'),
        mpatches.Patch(color='blue', label='Robot'),
        mpatches.Patch(color='red', label='Goal'),
    ]

    plt.legend(handles=legend_elements, loc='upper right', bbox_to_anchor=(1.4, 1))
    plt.title("Dynamic UGV Navigation")

    plt.pause(0.3)
    plt.clf()


# MAIN PROGRAM
if __name__ == "__main__":
    size = 10  # change to 70 later
    density = 0.2

    grid = generate_grid(size, density)

    start = (0, 0)
    goal = (size - 1, size - 1)

    grid[start[0]][start[1]] = 0
    grid[goal[0]][goal[1]] = 0

    current = start

    total_nodes_explored = 0
    replans = 0
    start_time = time.time()

    print("🤖 UGV Dynamic Navigation (Animated)\n")

    # Enable interactive plotting
    plt.ion()

    while current != goal:
        parent, nodes = astar(grid, current, goal)
        total_nodes_explored += nodes
        replans += 1

        path = get_path(parent, goal)

        if not path or len(path) < 2:
            print("❌ No path available! Mission failed.")
            break

        # Move robot
        current = path[1]

        # Add dynamic obstacle
        add_dynamic_obstacle(grid, current, goal)

        # Show animation
        visualize_grid(grid, path, current, goal)

        time.sleep(0.2)

    plt.ioff()
    plt.show()

    end_time = time.time()

    # Results
    print("\n📊 FINAL RESULTS:")

    if current == goal:
        print("Goal reached successfully!")
    else:
        print("Failed to reach goal")

    print(f"Total steps taken: {replans}")
    print(f"Total nodes explored: {total_nodes_explored}")
    print(f"Time taken: {end_time - start_time:.4f} seconds")