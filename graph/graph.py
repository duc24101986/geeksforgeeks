import Queue
# The graph class :
# vertex_list = {1: Vertex_object, 2: Vertex_object, 3: Vertex_object}
# vertex_object contains id and connectedTo = {1: weight, 2: weigth, 3: weight}

class Vertex:
    def __init__(self,key):
        self.id = key
        self.connectedTo = {}
    
    def addNeighbor(self, nbr, weight=0):
        self.connectedTo[nbr] = weight
    
    def __str__(self):
        return str(self.id) + ' connectedTo: ' + str([x.id for x in self.connectedTo])

    def getConnections(self):
        return self.connectedTo.keys()

    def getId(self):
        return self.id

    def getWeight(self,nbr):
        return self.connectedTo[nbr]

class Graph:
    def __init__(self):
        self.vertList = {}
        self.numVertices = 0
    
    def addVertex(self, key):
        newVertex = Vertex(key)
        self.vertList[key] = newVertex
        self.numVertices = self.numVertices + 1
        return newVertex
        
    def getVertex(self, n):
        if n in self.vertList:
            return self.vertList[n]
        else:
            return None
            
    def addEdge(self, f, t, cost=0):
        if f not in self.vertList:
            new_vertex = Vertex(f)
        if t not in self.vertList:
            new_vertex = Vertex(t)
        self.vertList[f].addNeighbor(self.vertList[t].getId(),cost)
    
    def printGraph(self):
        print "Vertex list:"
        print self.vertList.keys()
        
        for id in self.vertList.keys():
            vertex = self.vertList[id]
            print "Vertex: " + str(self.vertList[id].getId())
            print self.vertList[id].connectedTo








        





