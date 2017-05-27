from collections import defaultdict

class Graph:
    def __init__(self, n):
        self.nodes = n
        self.graph = defaultdict(list)

    def addEdge(self, u, v):
        self.graph[u].append(v)

    def DFSUtil(self, v, visited):
        visited[v] = True
        print v

        for i in self.graph[v]:
            if not visited[i]:
                self.DFSUtil(i, visited)

    def DFS(self, v):
        visited = [False] * self.nodes
        self.DFSUtil(v, visited)

        for i, val in enumerate(visited):
            if not val:
                self.DFSUtil(i, visited)


g = Graph(4)
g.addEdge(0, 1)
g.addEdge(0, 2)
g.addEdge(1, 2)
g.addEdge(2, 0)
g.addEdge(2, 3)
g.addEdge(3, 3)

g.DFS(2)

h = Graph(6)
h.addEdge(5, 2)
h.addEdge(5, 0)
h.addEdge(4, 0)
h.addEdge(4, 1)
h.addEdge(2, 3)
h.addEdge(3, 1)

print h.graph

h.DFS(5)
