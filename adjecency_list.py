class Graph:
    def __init__(self, vertices):
        self.vertices = vertices
        self.adj_list = {i: [] for i in range(vertices)}

    def add_edge(self, u, v):
        if 0 <= u < self.vertices and 0 <= v < self.vertices:
            self.adj_list[u].append(v)
            self.adj_list[v].append(u)  # For an undirected graph

    def remove_edge(self, u, v):
        if 0 <= u < self.vertices and 0 <= v < self.vertices:
            if v in self.adj_list[u]:
                self.adj_list[u].remove(v)
            if u in self.adj_list[v]:
                self.adj_list[v].remove(u)

    def has_edge(self, u, v):
        if 0 <= u < self.vertices and 0 <= v < self.vertices:
            return v in self.adj_list[u] and u in self.adj_list[v]
        else:
            return False

    def print_adj_list(self):
        for vertex, neighbors in self.adj_list.items():
            print(f"Vertex {vertex}: {neighbors}")

# Example usage:
num_vertices = 5
graph = Graph(num_vertices)

graph.add_edge(0, 1)
graph.add_edge(0, 2)
graph.add_edge(1, 3)
graph.add_edge(2, 4)

graph.print_adj_list()

# Check if there is an edge
if graph.has_edge(0, 1):
    print("There is an edge between nodes 0 and 1.")
else:
    print("There is no edge between nodes 0 and 1.")

# Remove an edge
graph.remove_edge(0, 1)

print("\nAfter removing the edge:")
graph.print_adj_list()
