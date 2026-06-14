"""
Wonjun Jo and AJ Thomas
"""

from modules.graph.graph import *
from graph_representations import *
from modules.utils.linkedQueue import *
from modules.utils.linkedStack import *

import random

# THIS IS THE GENERAL TRAVERSE FUNCTION, JUST CHANGES DATATYPE BASED ON DFS/BFS
def traverse(graph, start, dataType):
    result = []
    for vertex in graph.getVertices():
        vertex.mark = False
        
    startVertex = graph.getVertex(start) # the vertex object itself
    collection = dataType([startVertex])
    
    while not collection.isEmpty():
        currentVertex = collection.pop()
        if currentVertex.mark == False:
            currentVertex.mark = True
            result.append(str(currentVertex))
            for option in currentVertex.incidentEdges():
                optionVertex = option.getConnectedTo()
                if optionVertex.mark == False:
                    collection.add(optionVertex)
    return result

def BFS(graph, start):
    return traverse(graph, start, LinkedQueue)

def DFS(graph, start):
    return traverse(graph, start, LinkedStack)

def computeComponents(graph):
    components = dict()
    c = 0
    for vertex in graph.getVertices():
        
        if not str(vertex) in components:
            components[str(vertex)] = c
            sameComponentList = BFS(graph, vertex.label)
            for v in sameComponentList:
                
                components[v] = c

            c += 1
    
    return components


def testTraversal(graph, traversal, start):
    results = " ".join(traversal(graph, start))
    return results
    
def testTraversals():
    #g = getTestGraph()
    g = readEdgeList("graph1.txt")
    
    res = testTraversal(g, BFS, 'A')
    print(res)
    
    res = testTraversal(g, DFS, 'A')
    print(res)

def testComponents():
    #g = getTestGraph()
    g = readEdgeList("comp1.txt")
    
    comps = computeComponents(g)
    compNumb = max(comps.values())+1
    print("Number of components:", compNumb)
    print("Vertices and their component number:")
    for v in g.vertices:
        print(v, comps[v])
    
def main():
    testTraversals()
    #testComponents()
    
    
if __name__ == "__main__":
    main()

