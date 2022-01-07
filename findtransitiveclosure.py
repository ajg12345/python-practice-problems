"""
This problem was asked by Microsoft.

The transitive closure of a directed graph is a measure of which vertices are 
reachable from other vertices. It can be represented as a matrix M, 
where M[i][j] == 1 if there is a path between vertices i and j, and otherwise 0.

For example, suppose we are given the following graph in adjacency list form:

graph = [
    [0, 1, 2,  3],
    [1, 2],
    [2],
    [3]
]

The transitive closure of this graph would be:

[1, 1, 1, 1]
[0, 1, 1, 0]
[0, 0, 1, 0]
[0, 0, 0, 1]

Given a graph, find its transitive closure.
"""
# had to look this one up:
# first part is converting an adjacency list rep into a matrix rep,
# second part is passing that list into a object to find the transitive closure

# First part:
# Python3 program to implement
# the above approach

# Function to insert vertices
# to adjacency list
def insert(adj, u, v):

    # Insert a vertex v to vertex u
    adj[u].append(v)
    return


# Function to display adjacency list
def printList(adj, V):

    for i in range(V):
        print(i, end="")

        for j in adj[i]:
            print(" --> " + str(j), end="")

        print()

    print()


# Function to convert adjacency
# list to adjacency matrix
def convert(adj, V):

    # Initialize a matrix
    matrix = [[0 for j in range(V)] for i in range(V)]

    for i in range(V):
        for j in adj[i]:
            matrix[i][j] = 1

    return matrix


# Function to display adjacency matrix
def printMatrix(adj, V):

    for i in range(V):
        for j in range(V):
            print(adj[i][j], end=" ")

        print()

    print()


# Driver code
if __name__ == "__main__":

    V = 5

    adjList = [[] for i in range(V)]

    # Inserting edges
    insert(adjList, 0, 1)
    insert(adjList, 0, 4)
    insert(adjList, 1, 0)
    insert(adjList, 1, 2)
    insert(adjList, 1, 3)
    insert(adjList, 1, 4)
    insert(adjList, 2, 1)
    insert(adjList, 2, 3)
    insert(adjList, 3, 1)
    insert(adjList, 3, 2)
    insert(adjList, 3, 4)
    insert(adjList, 4, 0)
    insert(adjList, 4, 1)
    insert(adjList, 4, 3)

    # Display adjacency list
    print("Adjacency List: ")
    printList(adjList, V)

    # Function call which returns
    # adjacency matrix after conversion
    adjMatrix = convert(adjList, V)

    # Display adjacency matrix
    print("Adjacency Matrix: ")
    printMatrix(adjMatrix, V)

# This code is contributed by rutvik_56

# Second part:
# Python program for transitive closure using Floyd Warshall Algorithm
# Complexity : O(V^3)

from collections import defaultdict

# Class to represent a graph
class Graph:
    def __init__(self, vertices):
        self.V = vertices

    # A utility function to print the solution
    def printSolution(self, reach):
        print("Following matrix transitive closure of the given graph ")
        for i in range(self.V):
            for j in range(self.V):
                if i == j:
                    print("%7d\t" % (1))
                else:
                    print("%7d\t" % (reach[i][j]))
            print("")

    # Prints transitive closure of graph[][] using Floyd Warshall algorithm
    def transitiveClosure(self, graph):
        """reach[][] will be the output matrix that will finally
        have reachability values."""
        reach = [i[:] for i in graph]
        """Add all vertices one by one to the set of intermediate
        vertices.
         ---> Before start of a iteration, we have reachability value
         for all pairs of vertices such that the reachability values
          consider only the vertices in set 
        {0, 1, 2, .. k-1} as intermediate vertices.
          ----> After the end of an iteration, vertex no. k is
         added to the set of intermediate vertices and the 
        set becomes {0, 1, 2, .. k}"""
        for k in range(self.V):

            # Pick all vertices as source one by one
            for i in range(self.V):

                # Pick all vertices as destination for the
                # above picked source
                for j in range(self.V):

                    # If vertex k is on a path from i to j,
                    # then make sure that the value of reach[i][j] is 1
                    reach[i][j] = reach[i][j] or (reach[i][k] and reach[k][j])

        self.printSolution(reach)


g = Graph(4)

graph = [[1, 1, 0, 1], [0, 1, 1, 0], [0, 0, 1, 1], [0, 0, 0, 1]]

# Print the solution
g.transitiveClosure(graph)

# This code is contributed by Neelam Yadav

answergraph = [[1, 1, 1, 1], [0, 1, 1, 0], [0, 0, 1, 0], [0, 0, 0, 1]]

assert get_trans_closure(graph) == answergraph
