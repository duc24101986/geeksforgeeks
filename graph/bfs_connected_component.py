import Queue
from graph import Vertex, Graph


def createGraph():
    g = Graph()
    
    for index in range(10):
        g.addVertex(index)
    
    for start in range(0, 4):
            g.addEdge(start,start+1,1)
            g.addEdge(start+1,start,1)
            
    for start in range(5, 9):
            g.addEdge(start,start+1,1)
            g.addEdge(start+1,start,1)
    
    return g
    

def bfsConnectedComponent(g):   
    visited_vertex = []
    connected_component = {}
    component_id = 0
            
    for start_vertex in g.vertList.keys():
        if start_vertex in visited_vertex:
            continue
        
        vertices_queue = Queue.Queue()
        vertices_queue.put(start_vertex)
        
        while(not vertices_queue.empty()):
            current_vertex = vertices_queue.get()
            
            # mark visited
            visited_vertex.append(current_vertex)
            
            # mark component 
            connected_component[current_vertex] = component_id
            
            # Find nbr
            nbr = g.vertList[current_vertex].getConnections()
            
            for vertex in nbr:
                if vertex not in visited_vertex:
                    vertices_queue.put(vertex)  
        
        # Increase the component id:
        component_id = component_id + 1
                    
    print "Connected component: ",
    print connected_component


if __name__ == '__main__':

    g = createGraph()
    g.printGraph()
    bfsConnectedComponent(g)

