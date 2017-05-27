# Kahn's Algorithm for Topological Sorting
# http://www.geeksforgeeks.org/topological-sorting-indegree-based-solution/

# BFS kind off approach
# O(V+E)

from collections import defaultdict

class Graph:

    def __init__(self, vertices):
        self.vertices = vertices
        self.graph = defaultdict(list)

    def addEdge(self, u, v):
        self.graph[u].append(v)

    def topologicalSort(self):

        in_degree = [0] * self.vertices

        # Counting in-degrees for each node
        for i in xrange(self.vertices):
            for j in self.graph[i]:
                in_degree[j] += 1

        queue = []
        for i in xrange(self.vertices):
            if in_degree[i] == 0:
                queue.append(i)

        cnt = 0
        top_order = []

        while queue:
            u = queue.pop(0)
            top_order.append(u)

            for i in self.graph[u]:
                in_degree[i] -= 1
                if in_degree[i] == 0:
                    queue.append(i)
            cnt+=1
        if cnt != self.vertices:
            print "Cycle detected in DAG"
        else:
            print top_order

if __name__ == '__main__':
    g = Graph(6)
    g.addEdge(5, 2)
    g.addEdge(5, 0)
    g.addEdge(4, 0)
    g.addEdge(4, 1)
    g.addEdge(2, 3)
    g.addEdge(3, 1)

    g.topologicalSort()
