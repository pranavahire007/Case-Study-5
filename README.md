# Case-Study-5
# 🗺️ GPS Navigation System Using Graphs
> A simple Python-based GPS Navigation System developed using a Weighted Graph and Dijkstra's Shortest Path Algorithm to find the shortest route between locations.

---

## 🎯 Objective
The objective of this case study is to develop a GPS Navigation System using the **Graph data structure** and **Dijkstra's Shortest Path Algorithm** in Python.

The system represents locations as vertices and roads as weighted edges. It helps users find the shortest route between two locations based on road distances.

This project demonstrates how graph algorithms can be applied to real-world navigation systems to determine efficient routes between different places.

---

## 📖 Introduction
GPS navigation systems are widely used in applications such as Google Maps to find routes between locations. They help users travel efficiently by identifying suitable paths and calculating distances.

A graph is a non-linear data structure consisting of vertices and edges. In a navigation system, vertices represent locations, while edges represent roads connecting those locations. Each edge has a weight representing the distance between two locations.

In this project, a weighted graph is implemented using Python dictionaries. Users can add locations, connect them with roads, display the map, and find the shortest route between two locations.

The system uses **Dijkstra's Shortest Path Algorithm** to calculate the minimum total distance from a starting location to a destination. A priority queue helps process locations in increasing order of their current shortest distance.

This case study demonstrates the practical application of graphs and shortest-path algorithms in navigation systems.

---

## ✨ Features

| Feature | Description |
|---|---|
| 📍 Add Location | Adds a new location to the navigation map. |
| 🛣️ Add Road | Connects two locations with a specified road distance. |
| 🗺️ Display Map | Displays locations and their connected roads. |
| 🔍 Find Shortest Route | Calculates the shortest route between two locations. |
| 📏 Calculate Distance | Displays the total distance of the shortest route in kilometres. |
| 🔄 Bidirectional Roads | Allows travel between connected locations in both directions. |
| ⚠️ Invalid Input Handling | Handles invalid menu choices and invalid distance values. |
| 🚪 Exit | Terminates the program. |

---

## 🧩 Data Structure Used

### 1. Graph
A graph is used to represent the navigation network. Each location is a vertex, and each road is an edge connecting two locations.

### 2. Weighted Graph
Each road has a weight representing the distance between connected locations. These weights are used to calculate the shortest route.

### 3. Adjacency List
The graph is implemented using Python dictionaries. Each location stores its neighbouring locations and the distances to them. This representation is known as an adjacency list.

### 4. Priority Queue
A priority queue is used to select the location with the smallest known distance during Dijkstra's algorithm. Python's `heapq` module provides the required functionality.

### 5. Dijkstra's Shortest Path Algorithm
Dijkstra's algorithm finds the minimum-distance path from a starting location to a destination when all road weights are non-negative.

---

## 💻 Technology Used

- **Programming Language:** Python
- **IDE:** Visual Studio Code (VS Code)
- **Data Structure:** Weighted Graph
- **Graph Representation:** Adjacency List
- **Algorithm:** Dijkstra's Shortest Path Algorithm
- **Python Module:** `heapq`
- **Concepts:** Graph Traversal, Shortest Path, Priority Queue, and Weighted Edges

---

## ⚙️ Operations

1. **Add Location:** Adds a new location to the graph.
2. **Add Road:** Creates a bidirectional connection between two existing locations and assigns a distance to the road.
3. **Display Map:** Displays every location and its connected neighbouring locations with their road distances.
4. **Find Shortest Route:** Accepts a starting location and destination, then applies Dijkstra's algorithm to determine the minimum-distance route.
5. **Display Total Distance:** Shows the shortest route and its total distance in kilometres.
6. **Exit:** Ends the program.

---

## ▶️ How to Run

1. Install Python on your computer.
2. Open Visual Studio Code.
3. Create a folder named `GPS-Navigation-Using-Graphs`.
4. Create a Python file named `main.py`.
5. Copy the program code into `main.py`.
6. Open the terminal in VS Code.
7. Run the following command:

```bash
python main.py
```

8. Select an option from the menu and follow the instructions displayed on the screen.

**Note:** The program includes sample locations and roads when it starts, so you can test the shortest-path algorithm immediately.

---

## 📌 Learning Outcomes

- Understood the fundamentals of graph data structures.
- Learned how to represent a weighted graph using an adjacency list.
- Understood vertices, edges, and edge weights.
- Learned the working principle of Dijkstra's Shortest Path Algorithm.
- Understood the role of a priority queue in shortest-path calculations.
- Practised adding locations and connecting them with weighted roads.
- Learned how to reconstruct and display the shortest route.
- Understood how graph algorithms are applied in real-world navigation systems.

---

## 🎓 Conclusion
The GPS Navigation System demonstrates how graphs and shortest-path algorithms can be used to solve real-world route-finding problems. The system represents locations as vertices and roads as weighted edges, allowing users to manage a simple navigation network.

By implementing Dijkstra's Shortest Path Algorithm, the program identifies the route with the minimum total distance between two locations. The use of an adjacency list and a priority queue makes the implementation suitable for demonstrating fundamental graph concepts.

This case study provides practical knowledge of weighted graphs, shortest-path algorithms, and their applications in navigation systems. It is an educational simulation and does not use live GPS data or real-time traffic information.

---

### 👩‍💻 Developed as a Data Structures Case Study
**Python | Graph | Dijkstra's Algorithm | GPS Navigation System**
