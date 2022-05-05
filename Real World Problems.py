# A class to represent a graph object
class Graph:
    def __init__(self, edges, n):
        self.adjList = [[] for _ in range(n)]
 
        # add edges to the undirected graph
        for (i, j) in edges:
            self.adjList[i].append(j)
            self.adjList[j].append(i)
 
 
# Function to assign colors to vertices of a graph
def colorGraph(graph, n):
    result = {}
    # assign a color to vertex one by one
    for u in range(n):
 
        # check colors of adjacent vertices of `u` and store them in a set
        assigned = set([result.get(i) for i in graph.adjList[u] if i in result])
 
        # check for the first free color
        color = 1
        for c in assigned:
            if color != c:
                break
            color = color + 1
 
        # assign vertex `u` the first available color
        result[u] = color
 
    for v in range(n):
        print(f'Color assigned to vertex {v} is {colors[result[v]]}')
 
 
# Greedy coloring of a graph
if __name__ == '__main__':
 
    # Add more colors for graphs with many more vertices
    colors = ['', 'BLUE', 'GREEN', 'RED', 'YELLOW', 'ORANGE', 'PINK',
            'BLACK', 'BROWN', 'WHITE', 'PURPLE', 'VOILET']
 
    # List of graph edges as per the above diagram
    edges = [(0, 1), (0, 4), (0, 5), (4, 5), (1, 4), (1, 3), (2, 3), (2, 4)]
 
    # total number of nodes in the graph (labelled from 0 to 5)
    n = 6
 
    # build a graph from the given edges
    graph = Graph(edges, n)
 
    # color graph using the greedy algorithm
    colorGraph(graph, n)
    
    
    
    
    
    
    
    
    
    




import numpy as np
class Graph():
    def __init__(self, vertices):
        self.V = vertices
        self.graph = [[0 for column in range(vertices)]\
                              for row in range(vertices)]

    def isSafe(self, v, colour, c):
        for i in range(self.V):
            if self.graph[v][i] == 1 and colour[i] == c:
                return False
        return True
     

    def graphColourUtil(self, m, colour, v):
        if v == self.V:
            return True
        for c in range(1, m + 1):
            if self.isSafe(v, colour, c) == True:
                colour[v] = c
                if self.graphColourUtil(m, colour, v + 1) == True:
                    return True
                colour[v] = 0
 
    def graphColouring(self, m):
        colour = [0] * self.V
        if self.graphColourUtil(m, colour, 0) == None:
            return False
        print ("\nThe solution is")
        for c in colour:
            print ("Colour:",c,end=', ')
        return True

list_m=[]
n=int(input("Enter the number of nodes "))
f_list=[]
print("\nEnter the values of adjacency matrix.\ni.e.",n*n,"inputs sepereated by a space")
a=input()
list_m=a.split()
list_m = [int(i) for i in list_m]

list_m=(list_m)
f_list=np.array_split(list_m,n)
g=Graph(n)
g.graph=list(f_list)
m=int(input("\nEnter the chromatic number: "))
g.graphColouring(m)
