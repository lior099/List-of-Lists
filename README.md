# List-of-Lists

Lior Shifman and Haim Isakov

This repository is about our implementation of a Dataset called List of Lists(LOL), which can represent a Graph in python in a very memory efficient way.

NOTE: Currently it's a WORK IN PROGRESS which means some bugs are expected, and there is still no full documentaion of the project and how to use it.

# How to use?

For undirected graph:
'''

undirected_graph = LolGraph(directed=False, weighted=True).

undirected_graph.convert(edgeList) //For example: undirected_graph.convert([[1,2,3], [4,6,0.1]])
'''

For directed graph:
'''
directed_graph= DLGW(weighted=True).

directed_graph.convert(edgeList) //For example: directed_graph.convert([[1,2,3], [4,6,0.1]])
'''

Basically, you can use LolGraph class to create a directed graph, but some functions (in_degrees, predecessors) are not implemented in the most effecient way. 
Therefore, use LolGraph for undirected graph, and DLGW for directed graph.

The name of the implemented functions are the same as if you were using Networkx library.
