from collections import deque

class Graph:
    def __init__(self, num_vertices):
        self.num_vertices = num_vertices
        self.adj_matrix = [[0] * num_vertices for _ in range(num_vertices)]
        self.visited = [False] * num_vertices

    def add_edge(self, u, v):
        if 0 <= u < self.num_vertices and 0 <= v < self.num_vertices:
            self.adj_matrix[u][v] = 1
            self.adj_matrix[v][u] = 1  # For an undirected graph

    def bfs(self, start_vertex):
        queue = deque()
        queue.append(start_vertex)
        self.visited[start_vertex] = True

        while queue:
            current_vertex = queue.popleft()
            print(f"Visited vertex {current_vertex}")

            for neighbor in range(self.num_vertices):
                if self.adj_matrix[current_vertex][neighbor] == 1 and not self.visited[neighbor]:
                    queue.append(neighbor)
                    self.visited[neighbor] = True

# Example usage:
num_vertices = 5
graph = Graph(num_vertices)

graph.add_edge(0, 1)
graph.add_edge(0, 2)
graph.add_edge(1, 3)
graph.add_edge(2, 4)

start_vertex = 0
print(f"Breadth-First Traversal starting from vertex {start_vertex}:")
graph.bfs(start_vertex)
