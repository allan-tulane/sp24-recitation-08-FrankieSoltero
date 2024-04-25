from collections import deque
from heapq import heappush, heappop 
import heapq

def shortest_shortest_path(graph, source):
    """
    Params: 
      graph.....a graph represented as a dict where each key is a vertex
                and the value is a set of (vertex, weight) tuples (as in the test case)
      source....the source node
      
    Returns:
      a dict where each key is a vertex and the value is a tuple of
      (shortest path weight, shortest path number of edges). See test case for example.
    """
    
    ### TODO
    distance = {vertex: float('inf') for vertex in graph}
    path_length = {vertex: float('inf') for vertex in graph}
    
    priority_queue = [(0, source)]
    
    distance[source] = 0
    path_length[source] = 0
    
    while priority_queue:
        dist, current_vertex = heapq.heappop(priority_queue)
        
        for neighbor, weight in graph[current_vertex]:
            new_distance = dist + weight
            new_path_length = path_length[current_vertex] + 1
            
            if new_distance < distance[neighbor]:
                distance[neighbor] = new_distance
                path_length[neighbor] = new_path_length
                
                heapq.heappush(priority_queue, (new_distance, neighbor))
                
            elif new_distance == distance[neighbor] and new_path_length < path_length[neighbor]:
                path_length[neighbor] = new_path_length
                
    return {vertex: (distance[vertex], path_length[vertex]) for vertex in graph}
    pass
    

    
    
def bfs_path(graph, source):
    parent = {}  
    visited = {source}  
    queue = deque([source])  
    
    while queue:
        current_vertex = queue.popleft()
        for neighbor in graph[current_vertex]:
            if neighbor not in visited:
                visited.add(neighbor)
                parent[neighbor] = current_vertex 
                queue.append(neighbor)
    
    return parent
    ###TODO
    pass

def get_sample_graph():
     return {'s': {'a', 'b'},
            'a': {'b'},
            'b': {'c'},
            'c': {'a', 'd'},
            'd': {}
            }


    
def get_path(parents, destination):
  """
    Returns:
      The shortest path from the source node to this destination node 
      (excluding the destination node itself). See test case for example.
    """
  path = []

  while destination in parents:
    destination = parents[destination]
    path.insert(0, destination)
  return ''.join(path)
    ###TODO
pass
