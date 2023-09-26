class Graph:
    def __init__(self, num_vertices):
        self.num_vertices = num_vertices
        self.adj_matrix = [[0] * num_vertices for _ in range(num_vertices)]
        self.visited = [False] * num_vertices

    def add_edge(self, u, v):
        if 0 <= u < self.num_vertices and 0 <= v < self.num_vertices:
            self.adj_matrix[u][v] = 1
            self.adj_matrix[v][u] = 1  # For an undirected graph

    def dfs(self, start_vertex):
        self.visited[start_vertex] = True
        print(f"Visited vertex {start_vertex}")

        for neighbor in range(self.num_vertices):
            if self.adj_matrix[start_vertex][neighbor] == 1 and not self.visited[neighbor]:
                self.dfs(neighbor)

# Example usage:
num_vertices = 5
graph = Graph(num_vertices)

graph.add_edge(0, 1)
graph.add_edge(0, 2)
graph.add_edge(1, 3)
graph.add_edge(2, 4)

start_vertex = 0
print(f"Depth-First Traversal starting from vertex {start_vertex}:")
graph.dfs(start_vertex)
