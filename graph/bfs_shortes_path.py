import Queue
from graph import Vertex, Graph

def createGraph():
    g = Graph()
    
    for index in range(10):
        g.addVertex(index)
    
    for start in range(1, 9):
            g.addEdge(start,start+1,1)
            g.addEdge(start+1,start,1)
    
    return g
    
# using bsf traversal to find the shortest path
# graph is directed and unweight
def bsfShortestPath(g, start, end):
    vertices_queue = Queue.Queue()
    vertices_queue.put(start)
    
    shortest_path = []
    
    while(not vertices_queue.empty()):
        current_vertex = vertices_queue.get()
        
        shortest_path.append(current_vertex)
        
        if current_vertex == end:
            break
        
        # Find nbr
        nbr = g.vertList[current_vertex].getConnections()
        
        for vertex in nbr:
            if vertex not in shortest_path:
                vertices_queue.put(vertex)           
                
    print "The shortest path ",
    print shortest_path
    



    
if __name__ == '__main__':

    g = createGraph()
    g.printGraph()
    bsfShortestPath(g, 5, 8)