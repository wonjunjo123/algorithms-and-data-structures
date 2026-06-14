from ..set.arraySet import ArraySet

class LinkedEdge(object):
   def __init__(self, fromVertex, toVertex, weight = None):
      self.vertex1 = fromVertex
      self.vertex2 = toVertex
      self.weight = weight
      self.mark = False
   
   def __eq__(self, other):
      if self is other:
         return True
      if type(self) != type(other):
         return False
      return self.vertex1 == other.vertex1 and self.vertex2 == other.vertex2
   
   def getConnectedTo(self):
      return self.vertex2
   
   def getConnectedFrom(self):
      return self.vertex1
   
   def getOtherVertex(self, vertex):
      if self.vertex1 == vertex:
         return self.vertex2
      
      return self.vertex1
   
   def __str__(self):
      return str(self.vertex1) + ">" + str(self.vertex2) + ":" + str(self.weight)

class LinkedVertex(object):
   
   def __init__(self, label, coords=None):
      self.label = label
      self.edgeList = []
      self.mark = False
   
   def setLabel(self, label, g):
      g.vertices.pop(self.label, None)
      g.vertices[label] = self
      self.label = label
   
   def neighboringVertices(self):
      vertices = []
      
      for edge in self.edgeList:
         vertices.append(edge.getOtherVertex(self))
      
      return iter(vertices)
   
   def addEdgeTo(self, toVertex, weight=None):
      self.edgeList.append(LinkedEdge(self, toVertex, weight))
   
   def removeEdgeTo(self, toVertex, weight=None):
      edge = LinkedEdge(self, toVertex, weight)
      if edge in self.edgeList:
         self.edgeList.remove(edge)
         return True
      else:
         return False
   
   def clearEdges(self):
      self.edgeList = []
      
   def getEdgeTo(self, toVertex, weight = None):
      edge = LinkedEdge(self, toVertex, weight)
      for e in self.edgeList:
         if e == edge:
            return e
      return None
   
   def incidentEdges(self):
      return self.edgeList
   

   def __str__(self):
      return str(self.label)
   
   
   def __hash__(self):
      return hash(self.label)
   

class LinkedDirectedGraph(object):
   def __init__(self):
      self.edgeCount = 0
      self.vertices = {}
      self.size = 0
   
   def clear(self):
      vKeys = list(self.vertices.keys())
      for vertex in range(len(vKeys)):
         self.removeVertex(vKeys[vertex])
         self.size = 0
         self.edgeCount = 0
   
   def clearEdges(self):
      for vertex in self.vertices.values():
         vertex.clearEdges()
      
      self.edgeCount = 0      
      
   def getVertex(self, label):
      return self.vertices.get(label, None)
   
   def getVertices(self):
      return self.vertices.values()
      
   def addVertex(self, label):
      self.vertices[label] = LinkedVertex(label)
      self.size += 1
   
   def removeVertex(self, label):
      removedVertex = self.vertices.pop(label, None)
      
      if removedVertex is None:
         return False
      for vertex in self.getVertices():
         if vertex.removeEdgeTo(removedVertex):
            self.edgeCount -= 1
      
      for edge in removedVertex.incidentEdges():
         self.edgeCount -= 1
      
      self.size -= 1
      return True
         
   def addEdge(self, fromLabel, toLabel, weight=None):
      fromVertex = self.vertices[fromLabel]
      toVertex = self.vertices[toLabel]
      if not fromVertex.getEdgeTo(toVertex):
         fromVertex.addEdgeTo(toVertex, weight)
         self.edgeCount += 1
      
   def getEdge(self, fromLabel, toLabel, weight=None):
      fromVertex = self.vertices[fromLabel]
      toVertex = self.vertices[toLabel]
      return fromVertex.getEdgeTo(toVertex, weight)
      
   
   def removeEdge(self, fromLabel, toLabel, weight=None):
      fromVertex = self.vertices[fromLabel]
      toVertex = self.vertices[toLabel]
      
      if fromVertex.removeEdgeTo(toVertex, weight):
         self.edgeCount -= 1
         return True
      
      return False
   
   def edges(self):
      # I want it to return a list of all the edge objects in the graph
      listOfEdges = []
      for vertex in self.getVertices(): # vertex is a vertex object
         for edge in vertex.incidentEdges(): # for edge object in edgeList of vertex object
            listOfEdges.append(edge)
      return listOfEdges
   
   def hasEdge(self, v1, v2):
      # checks if there is a edge in between v1(from) and v2(to)
      if v2 in v1.incidentEdges():
         return True
      
      return False

   def __str__(self):
      result = ''
      for vertex in self.getVertices():
         result2 = ''
         for edge in vertex.incidentEdges():
            result2 += str(edge) + ' / '
         result += '{}: {}\n'.format(str(vertex), result2)
      return result 

   
class LinkedUndirectedGraph(LinkedDirectedGraph):
   def __init__(self):
      super().__init__()
   
      
   def addEdge(self, fromLabel, toLabel, weight=None):
      super().addEdge(fromLabel, toLabel, weight)
      super().addEdge(toLabel, fromLabel, weight)
   
   
   
   def removeEdge(self, fromLabel, toLabel, weight=None):
      super.removeEdge(fromLabel, toLabel, weight)
      super.removeEdge(toLabel, fromLabel, weight)


