from collections import defaultdict
class Graph:
    
    def __init__(self):
        self.graph = defaultdict(list)

    def addEdge(self, u, v):
        self.graph[u].append(v)

    def DFSUtil(self, v, visited):

        visited.add(v)
        print(v, end=' ')
        for neighbour in self.graph[v]:
            if neighbour not in visited:
                self.DFSUtil(neighbour, visited)
    
    def DFS(self, v):
        visited = set()
        self.DFSUtil(v, visited)

g = Graph()
n=int(input("Enter the number of vertex: "))
for i in range(n):
    print(f'\nEnter the number of transitions from {i}: ')
    t=int(input())
    for j in range(t):
        te=int(input(f"Enter the transition destination from {i}: "))
        g.addEdge(i,te)

sour=int(input("Enter the destination: "))
print(f"\nThe path to {sour} using DFS is ")
g.DFS(sour)
