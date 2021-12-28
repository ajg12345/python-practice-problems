"""
This problem was asked by Google.

Given an undirected graph represented as an adjacency matrix and an integer k, 
write a function to determine whether each vertex in the graph can be colored
 such that no two adjacent vertices share the same color using at most k colors.
"""
#just went to Geeks for Geeks on this one:  https://www.dailycodingproblem.com/blog/graph-coloring/
def valid(graph, colors):
    last_vertex, last_color = len(colors) - 1, colors[-1]
    colored_neighbors = [i for i, has_edge in enumerate(graph[last_vertex])
                            if has_edge and i < last_vertex]
    for neighbor in colored_neighbors:
        if colors[neighbor] == last_color:
            return False
    return True

def colorable(graph, k, colors=[]):
    #simple case, where there are the same number of colors as nodes
    if len(colors) == len(graph):
        return True

    for i in range(k):
        colors.append(i)
        if valid(graph, colors):
            if colorable(graph, k, colors):
                return True
        colors.pop()

    return False
