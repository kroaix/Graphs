class Queue():
    def __init__(self):
        self.queue = []
    def enqueue(self, value):
        self.queue.append(value)
    def dequeue(self):
        if self.size() > 0:
            return self.queue.pop(0)
        else:
            return None
    def size(self):
        return len(self.queue)

class Graph:
    def __init__(self):
        self.vertices = {}
        self.len = 0

    def add_vertex(self, vertex_id):
        self.vertices[vertex_id] = set()
        self.len += 1

    def add_edge(self, v1, v2):
        self.vertices[v1].add(v2)

    def get_neighbors(self, vertex_id):
        return self.vertices[vertex_id]

    def dfs(self, starting_vertex):
        queue = Queue()
        visited = set()
        
        path = []

        queue.enqueue(starting_vertex)

        while queue.size() > 0:
            current_vertex = queue.dequeue()
            if current_vertex not in visited:           
                path.append(current_vertex)
                visited.add(current_vertex)
                neighbors = self.get_neighbors(current_vertex)

                for neighbor in neighbors:
                    queue.enqueue(neighbor)

        return path

def earliest_ancestor(ancestors, starting_node):
    graph = Graph()

    for i in ancestors:
        graph.add_vertex(i[0])
        graph.add_vertex(i[1])
     
    for i in ancestors:
        graph.add_edge(i[1], i[0])    
        
    path = graph.dfs(starting_node)

    if len(path) == 1:
        return -1

    return path[-1]