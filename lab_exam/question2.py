from collections import deque

class Graph:
    def __init__(self):
        self.adj_list = {}

    def add_edge(self, v, w):
        if u not in self.adj_list:
            self.adj_list[v] = []
        self.adj_list[v].append(w)
        if v not in self.adj_list:
            self.adj_list[w] = []
        self.adj_list[w].append(v)

    def bfs(self, start_vertex):
        visited = set()           
        queue = deque()           
        visited.add(start_vertex)
        queue.append(start_vertex)
        traversal_order = []      
        while queue:
            vertex = queue.pop()
            traversal_order.append(vertex)
            for neighbor in self.adj_list.get(vertex, []):
                if neighbor not in visited:
                    visited.add(neighbor)
                    queue.append(neighbor)
        print(traversal_order)

    def display(self):
        for vertex in self.adj_list:
            print(f"{vertex} -> {self.adj_list[vertex]}")


g = Graph()
g.add_edge(0, 1)
g.add_edge(0, 2)
g.display()
g.bfs(0)

