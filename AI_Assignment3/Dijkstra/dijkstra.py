import csv
import heapq

# Load Graph from CSV
def load_graph(filename):
    graph = {}

    with open(filename, 'r') as file:
        reader = csv.DictReader(file)

        for row in reader:
            city1 = row["Origin"]
            city2 = row["Destination"]
            dist = int(row["Distance"])

            if city1 not in graph:
                graph[city1] = {}
            if city2 not in graph:
                graph[city2] = {}

            graph[city1][city2] = dist
            graph[city2][city1] = dist

    return graph


# Dijkstra Algorithm
def dijkstra(graph, start):
    pq = [(0, start)]
    distances = {node: float('inf') for node in graph}
    parent = {node: None for node in graph}

    distances[start] = 0

    while pq:
        current_cost, current_node = heapq.heappop(pq)

        for neighbor, weight in graph[current_node].items():
            cost = current_cost + weight

            if cost < distances[neighbor]:
                distances[neighbor] = cost
                parent[neighbor] = current_node
                heapq.heappush(pq, (cost, neighbor))

    return distances, parent


# Path Reconstruction
def get_path(parent, target):
    path = []
    while target:
        path.append(target)
        target = parent[target]
    return path[::-1]


# MAIN PROGRAM
if __name__ == "__main__":
    graph = load_graph("data/india_cities.csv")

    start_city = input("Enter starting city: ").strip()
    goal_city = input("Enter destination city: ").strip()

    if start_city not in graph:
        print("\Starting city not found in dataset!")
    elif goal_city not in graph:
        print("Destination city not found in dataset!")
    else:
        distances, parent = dijkstra(graph, start_city)

        path = get_path(parent, goal_city)

        print("\nRESULT:")
        print(f"Shortest path from {start_city} to {goal_city}:")
        print(" ➝  ".join(path))
        print(f"Total distance: {distances[goal_city]} km")