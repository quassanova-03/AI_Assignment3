# AI Assignment 3

## 1. DIJKSTRA'S 

### Overview
This project implements Dijkstra's Algorithm (Uniform Cost Search) to find the shortest path between cities in India using approximate real-world road distances derived from public datasets.
The cities are represented as nodes in the graph and the roads between them are weighted edges based on distance.
### What is Dijkstra's Algorithm?
Dijkstra's Algorithm is a greedy search algorithm used to find the shortest path between weighted nodes in a graph.

It works by:
- Expanding the node with the lowesr cumulative cost
- Updating distances to neighbour nodes
- Repeating until destination is reached

This search method, in AI, is also known as Uniform Cost Search.

### Problem Representation
- Cities → Nodes
- Roads → Edges
- Distance → Edge weights
The graph is implemented using an adjacency list.

### How the program works
1. Initialize all distances to infinity.
2. Set the starting node distance to 0.
3. Use a priority queue (minheap) to extract node with minimum distance.
4. Update distances of all the neighbouring nodes.
5. Repeat until all nodes are processed.

### Project Structure
```
Dijkstra/
│
├── data/
│ └── india_cities.csv
│
├── dijkstra.py
│
└── README.md
```
- Language : Python
- Data Structure : Graph (Dictionary/Adjacency list)
- Input : CSV file containing city distances
- Time Complexity : O((V + E) log V
  - V = number of cities
  - E = number of roads

### How to run the code
1. Navigate to the directory
   ```
   cd AI_Assignment3/Dijkstra
   ```
2. Run the python file
   ```
   python dijkstra.py
   ```
   or
   ```
   py dijkstra.py
   ```
The program will print the solution path using Dijkstra's Algorithm.

### Applications
- GPS Navigation Systems (Google Maps)
- Network Routing
- Logistics and Supply Chain Optimization
- Urban Planning

### Conclusion
Dijkstra’s Algorithm efficiently computes the shortest path in a weighted graph.
This project demonstrates its application in real-world road networks, providing accurate and optimal routes between cities.

### Output
<img width="631" height="399" alt="image" src="https://github.com/user-attachments/assets/031e3b7e-eb67-435a-ba7e-619315628f46" />

## 2. UNMANNED GROUND VEHICLE (A* IMPLEMENTATION)

### Overview
This project simulates an Unmanned Ground Vehicle (UGV) navigating through a grid-based battlefield environment. The UGV finds the shortest path from a start position to a goal position while avoiding obstacles using the A* (A-star) algorithm.

This algorithm enables a UGV to:
- Navigate a grid environment  
- Avoid known obstacles  
- Reach the goal using the shortest possible path

### What is the A* Algorithm (Similar for part 3)
A* is a best-first search algorithm that finds the shortest path using:
<img width="582" height="122" alt="image" src="https://github.com/user-attachments/assets/862b0295-1647-4b22-bef9-0ef1052ae9d7" />
Where:

- f(n): Total estimated cost of the path through node
- g(n): Actual cost from the start node to current node
- h(n): Heuristic estimate of the cost to the goal

Heuristic Used :
Manhatten distance:
<img width="531" height="97" alt="image" src="https://github.com/user-attachments/assets/27dbaa36-43d6-4020-9ccc-ede2b9b9026f" />

Where:
- x1, y1 : Coordinates of node n
- x2, y2 : Coordinates of the goal node

### State Representation
- Grid-based environment (N x N)
- Each cell represents:
  - Free Space
  - Obstacl
  - Start
  - Goal

### Project Features
- Implementation of A\* algorithm for shortest path  
- Random generation of static obstacles
- Efficient grid-based pathfinding  
- Path reconstruction from start to goal

### Visualization
This project uses Matplotlib to visualize the grid and pathfinding results.

Color Representation:
- 🟩 Green → Start node
- 🟥 Red → Goal node
- 🟨 Yellow → Shortest path
- ⬛ Black → Obstacles
- ⬜ White → Free space

### Project Structure
```
AI_Assignment3
|
└── UGV
    |
    └── ugv_obstacle.py
```

### How it works
1. A grid of size N x N is created.
2. Node is evaluated using A*.
3. Manhattan distance is used to calculate heuristic.
4. The algorithm explores the nodes using a priority queue.
5. Nodes marked as obstacles are ignored during traversal.
6. Once the goal is reached, the path is traced back using parent pointers.

### How it runs
1. Navigate to the directory
   ```
   cd AI_Assignment3/UGV
   ```
2. Run the python file
   ```
   python ugv_obstacle.py
   ```
   or
   ```
   py ugv_obstacle.py
   ```
### Output
<img width="701" height="562" alt="image" src="https://github.com/user-attachments/assets/1dfb6c01-8fc3-43f8-8660-37caeb40b821" />

### Applications
- Autonomous robot navigation
- Path planning in robotics
- Game AI and simulations
- Grid-based navigation systems

### Conclusion
This project demonstrates how the A* algorithm can efficiently compute the shortest path in a grid environment with known obstacles.
The use of Matplotlib visualization enhances understanding and provides a clear representation of the navigation process.

## 3. UNMANNED GROUND VEHICLE WITH DYNAMIC OBSTACLES

### Overview
This project simulates an Unmanned Ground Vehicle (UGV) navigating through a grid-based battlefield environment with dynamic obstacles.

Unlike static environments, obstacles are not known beforehand and may appear during navigation. The UGV continuously updates its path in real-time using the A* (A-star) algorithm.

This algorithm enables a UGV to:
- Navigate a grid environment
- Adapt to changing surroundings
- Avoid dynamically appearing obstacles
- Reach the goal using the shortest possible path

### State representation
- Grid-based environment (N x N)
- Each cell represents:
  - Free Space
  - Obstacle (can change dynamically)
  - Robot (current position)
  - Goal

### Project Features
- Implementation of A* algorithm for shortest path  
- Dynamic obstacle generation during execution  
- Real-time path replanning  
- Efficient grid-based navigation  
- Continuous robot movement toward goal  

### Visualization
This project uses Matplotlib to visualize the grid and navigation process dynamically.

Color Representation:
- 🟦 Blue → Robot (UGV)
- 🟥 Red → Goal node
- 🟨 Yellow → Current path
- ⬛ Black → Obstacles
- ⬜ White → Free space

### Project Structure
```
AI_Assignment3
|
└── UGV_Dynamic
    |
    └── ugv_dynamic.py
```

### How it works
### How it works
1. A grid of size N x N is created.  
2. The robot starts at the initial position.  
3. A* computes the shortest path to the goal.  
4. The robot moves one step along the path.  
5. New obstacles may appear dynamically.  
6. If the path is blocked, A* is executed again.  
7. This process repeats until the goal is reached.

### How it runs
1. Navigate to the directory
   ```
   cd AI_Assignment3/UGV_Dynamic
   ```
2. Run the python file
   ```
   python ugv_dynamic.py
   ```
   or
   ```
   py ugv_dynamic.py
   ```
### Applications
- Military UGV navigation
- Autonomous vehicles
- Robotics and AI path planning
- Search and rescue missions

### Conclusion
This project demonstrates how the A* algorithm can be extended to dynamic environments.
By continuously replanning paths in response to changes, the UGV is able to navigate effectively even when obstacles are unknown or changing, making it suitable for real-world applications.
