from collections import deque
class Graph:

    def __init__(self, edges, x, n):
        self.adjList = [[] for _ in range(3*n)]
        for (v, u, weight) in edges:
            if weight == 3*x:
                self.adjList[v].append(v + n)
                self.adjList[v + n].append(v + 2*n)
                self.adjList[v + 2*n].append(u)
            elif weight == 2*x:
                self.adjList[v].append(v + n)
                self.adjList[v + n].append(u)
            else:
                self.adjList[v].append(u)
                
def printPath(predecessor, v, cost, n):
 
    if v >= 0:
        cost = printPath(predecessor, predecessor[v], cost, n)
        cost = cost + 1
        if v < n:
            print(v, end=' ')
    return cost
    
def findLeastPathCost(graph, source, dest, n):
    discovered = [False] * 3 * n
    discovered[source] = True
    predecessor = [-1] * 3 * n
    q = deque()
    q.append(source)
    while q:
        curr = q.popleft()
        if curr == dest:
            print(f'The least-cost path between {source} and {dest} is ', end='')
            print('having cost', printPath(predecessor, dest, -1, n))
        for v in graph.adjList[curr]:
            if not discovered[v]:
                discovered[v] = True
                q.append(v)
                predecessor[v] = curr
 
 
if __name__ == '__main__':
 
    x = 1
    edges = [
        (0, 1, 4*x), (0, 2, 1*x), (1, 3, 3*x), (2, 3, 2*x),
        (1, 4, 8*x), (3, 4, 4*x), (2, 5, 6*x), (5, 6, 8*x), (4, 6, 2*x)
    ]
 
    n = 7
    source = 0
    dest = 6
    graph = Graph(edges, x, n)
    findLeastPathCost(graph, source, dest, n)
