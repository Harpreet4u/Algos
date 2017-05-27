# Only DAGs support topological sorting
# O(V+E) time complexity

from collections import defaultdict

class Graph:

    def __init__(self, vertices):
        self.graph = defaultdict(list)
        self.vertices = vertices

    def addEdge(self, u, v):
        self.graph[u].append(v)

    def topologicalSortUtil(self, v, visited, stack):
        visited[v] = True

        for i in self.graph[v]:
            if not visited[i]:
                self.topologicalSortUtil(i, visited, stack)

        stack.insert(0, v)

    def topologicalSort(self):
        visited = [False] * self.vertices
        stack = []

        for i in xrange(self.vertices):
            if not visited[i]:
                self.topologicalSortUtil(i, visited, stack)

        print stack


if __name__ == '__main__':
    g = Graph(6)
    g.addEdge(5, 2)
    g.addEdge(5, 0)
    g.addEdge(4, 0)
    g.addEdge(4, 1)
    g.addEdge(2, 3)
    g.addEdge(3, 1)

    g.topologicalSort()
