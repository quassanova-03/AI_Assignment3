# AI Assignment 3

## 1. DIJKSTRA'S ALGORITHM
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

## 
