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
    
def bfs(graph, start):
    vetices_queue = Queue.Queue()
    vetices_queue.put(start)
    
    path= []

    while(not vetices_queue.empty()):
        # depop the queue
        current_vertex = vetices_queue.get()
        # mark the vertex as visited
        path.append(current_vertex)
        # Find the nbr
        nbr = graph.getVertex(current_vertex).connectedTo.keys()
        
        for nbr_vertex in nbr:
            if nbr_vertex not in path:
                vetices_queue.put(nbr_vertex)
                
    print path
    
if __name__ == '__main__':

    g = createGraph()
    g.printGraph()
    bfs(g, 5)