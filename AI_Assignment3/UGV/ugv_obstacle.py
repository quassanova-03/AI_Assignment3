import random
import heapq
import time
import matplotlib.pyplot as plt
import numpy as np
from matplotlib.colors import ListedColormap
import matplotlib.patches as mpatches

# Generate Grid with Obstacles
def generate_grid(size, density):
    grid = [[0 for _ in range(size)] for _ in range(size)]

    for i in range(size):
        for j in range(size):
            if random.random() < density:
                grid[i][j] = 1  # obstacle

    return grid


# A* Algorithm
def astar(grid, start, goal):
    rows, cols = len(grid), len(grid[0])

    def heuristic(a, b):
        return abs(a[0] - b[0]) + abs(a[1] - b[1])

    pq = [(0, start)]
    g_cost = {start: 0}
    parent = {start: None}

    visited_nodes = 0
    directions = [(0,1),(1,0),(-1,0),(0,-1)]

    while pq:
        _, current = heapq.heappop(pq)
        visited_nodes += 1

        if current == goal:
            return parent, visited_nodes

        for d in directions:
            nx, ny = current[0] + d[0], current[1] + d[1]

            if 0 <= nx < rows and 0 <= ny < cols:
                if grid[nx][ny] == 1:
                    continue

                new_cost = g_cost[current] + 1

                if (nx, ny) not in g_cost or new_cost < g_cost[(nx, ny)]:
                    g_cost[(nx, ny)] = new_cost
                    priority = new_cost + heuristic((nx, ny), goal)
                    heapq.heappush(pq, (priority, (nx, ny)))
                    parent[(nx, ny)] = current

    return None, visited_nodes


# Reconstruct Path
def get_path(parent, goal):
    if parent is None or goal not in parent:
        return []

    path = []
    while goal:
        path.append(goal)
        goal = parent.get(goal)

    return path[::-1]


# Print Grid (Terminal)
def print_grid(grid, path, start, goal):
    path_set = set(path)

    for i in range(len(grid)):
        for j in range(len(grid[0])):
            if (i, j) == start:
                print("S", end=" ")
            elif (i, j) == goal:
                print("G", end=" ")
            elif (i, j) in path_set:
                print("*", end=" ")
            elif grid[i][j] == 1:
                print("X", end=" ")
            else:
                print(".", end=" ")
        print()


# Visualize Grid
def visualize_grid(grid, path, start, goal):
    grid_np = np.array(grid)

    # Mark path
    for (i, j) in path:
        grid_np[i][j] = 2

    # Mark start and goal
    grid_np[start[0]][start[1]] = 3
    grid_np[goal[0]][goal[1]] = 4

    # Custom colors
    cmap = ListedColormap([
        "white",   # 0 = empty
        "black",   # 1 = obstacle
        "yellow",  # 2 = path
        "green",   # 3 = start
        "red"      # 4 = goal
    ])

    plt.imshow(grid_np, cmap=cmap)
    plt.title("UGV Pathfinding (A*)")

    # Legend
    legend_elements = [
        mpatches.Patch(color='white', label='Free Space'),
        mpatches.Patch(color='black', label='Obstacle'),
        mpatches.Patch(color='yellow', label='Path'),
        mpatches.Patch(color='green', label='Start'),
        mpatches.Patch(color='red', label='Goal'),
    ]

    plt.legend(handles=legend_elements, loc='upper right', bbox_to_anchor=(1.4, 1))
    plt.show()


# MAIN PROGRAM
if __name__ == "__main__":
    size = 10  # change to 70 later

    density_levels = {
        "low": 0.1,
        "medium": 0.25,
        "high": 0.4
    }

    print("Obstacle Density Levels: low / medium / high")
    level = input("Enter density level: ").lower()

    if level not in density_levels:
        print("Invalid choice!")
        exit()

    grid = generate_grid(size, density_levels[level])

    start = (0, 0)
    goal = (size - 1, size - 1)

    # Ensure start & goal are free
    grid[start[0]][start[1]] = 0
    grid[goal[0]][goal[1]] = 0

    start_time = time.time()

    parent, visited_nodes = astar(grid, start, goal)

    end_time = time.time()

    path = get_path(parent, goal)

    print("\nGRID:\n")
    print_grid(grid, path, start, goal)

    print("\nMeasures of Effectiveness:")

    if path:
        print("Path found!")
        print(f"Path length: {len(path)}")
    else:
        print("No path found")

    print(f"Nodes explored: {visited_nodes}")
    print(f"Time taken: {end_time - start_time:.6f} seconds")

    # SHOW VISUALIZATION
    visualize_grid(grid, path, start, goal)