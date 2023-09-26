class Graph:
    def __init__(self, vertices):
        self.vertices = vertices
        self.adj_matrix = [[0] * vertices for _ in range(vertices)]

    def add_edge(self, u, v):
        if 0 <= u < self.vertices and 0 <= v < self.vertices:
            self.adj_matrix[u][v] = 1
            self.adj_matrix[v][u] = 1  # For an undirected graph

    def remove_edge(self, u, v):
        if 0 <= u < self.vertices and 0 <= v < self.vertices:
            self.adj_matrix[u][v] = 0
            self.adj_matrix[v][u] = 0  # For an undirected graph

    def has_edge(self, u, v):
        if 0 <= u < self.vertices and 0 <= v < self.vertices:
            return self.adj_matrix[u][v] == 1
        else:
            return False

    def print_adj_matrix(self):
        for row in self.adj_matrix:
            print(" ".join(map(str, row)))

# Example usage:
num_vertices = 5
graph = Graph(num_vertices)

graph.add_edge(0, 1)
graph.add_edge(0, 2)
graph.add_edge(1, 3)
graph.add_edge(2, 4)

graph.print_adj_matrix()

# Remove an edge
graph.remove_edge(1,3)

print("\nAfter removing the edge:")
graph.print_adj_matrix()

# Check if there is an edge
if graph.has_edge(0, 1):
    print("There is an edge between nodes 0 and 1.")
else:
    print("There is no edge between nodes 0 and 1.")