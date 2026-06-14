"""
Wonjun Jo and AJ Thomas
"""

from modules.graph.graph import *
import random

'''
This is the hardcoded graph which should correspond to graph1.
The weights are randomized though.
'''
def getTestGraph(graphType=LinkedUndirectedGraph):
   """A random-ish graph with interesting pathing."""
   
   graph = graphType()
 
   graph.addVertex("A") 
   graph.addVertex("B")
   graph.addVertex("C") 
   graph.addVertex("D") 
   graph.addVertex("E") 
   graph.addVertex("F")
   graph.addVertex("G") 
   graph.addVertex("H") 
   graph.addVertex("I")
   graph.addVertex("J")
   graph.addVertex("K") 
   graph.addVertex("L")
   
   for pair in ["AB", "CB", "AG", "FE", "GC", "FI", "HF", "BH", "JL", "JD", "JE", "ED", "LA", "CD", "DG", "IJ", "CK", "KF"]:
      vertI = graph.getVertex(pair[0]) # vertI and J are the vertex objects themselves
      vertJ = graph.getVertex(pair[1])
      graph.addEdge(pair[0], pair[1], random.randint(1,5))
      
   return graph


def writeAdjacencyList(graph, outFileName):
   result = ''
   for vertex in graph.getVertices():
      edges = ''
      for edge in vertex.incidentEdges():
         edges += str(edge.getConnectedTo()) + '\n'
      result += '{} {}\n{}'.format(str(vertex), len(vertex.incidentEdges()), edges)
      
   with open(outFileName, 'w') as f:
      f.write(result)
      f.close()

def writeEdgeList(graph, outFileName):
   result = ''
   for edge in graph.edges():
      result += '{} {} {}\n'.format(str(edge.getConnectedFrom()), str(edge.getConnectedTo()), edge.weight)
      
   with open(outFileName, 'w') as f:
      f.write(result)
      f.close()

def readAdjacencyList(fileName):
   graph = LinkedUndirectedGraph()
   vertexSet = set()   
   with open(fileName, 'r') as f:

      while True:
         line = f.readline().split()
         if len(line) > 1:
            fromLabel = line[0]
            if not fromLabel in vertexSet:
               vertexSet.add(fromLabel)
               graph.addVertex(fromLabel)
               
         elif len(line) == 1:
            toLabel = line[0]
            if not toLabel in vertexSet:
               vertexSet.add(toLabel)
               graph.addVertex(toLabel)
            graph.addEdge(fromLabel, toLabel)
            
         else:
            break
         
      f.close()
         
   return graph
    
def readEdgeList(fileName):
   graph = LinkedUndirectedGraph()
   vertexSet = set()
   
   with open(fileName, 'r') as f:
      
      while True:
         lyst = f.readline().split()
         if lyst == []:
            break
         fromLabel, toLabel, weight = lyst
         
         if not fromLabel in vertexSet:
            vertexSet.add(fromLabel)
            graph.addVertex(fromLabel)
         if not toLabel in vertexSet:
            vertexSet.add(toLabel)
            graph.addVertex(toLabel)
            
         graph.addEdge(fromLabel, toLabel, weight)

      f.close()
      
   return graph
    
def main():
    g = getTestGraph()
    #writeAdjacencyList(g, "1.txt")
    writeEdgeList(g, "2.txt")
    #g2 = readAdjacencyList("1.txt")
    g3 = readEdgeList("2.txt")
    
    print(g)
    #print(g3)
    
if __name__ == "__main__":
    main()
