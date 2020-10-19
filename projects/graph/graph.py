"""
Simple graph implementation
"""
from util import Stack, Queue  # These may come in handy

class Graph:

    """Represent a graph as a dictionary of vertices mapping labels to edges."""
    def __init__(self):
        self.vertices = {}

    def add_vertex(self, vertex_id):
        """
        Add a vertex to the graph.
        """
        self.vertices[vertex_id] = set()

    def add_edge(self, v1, v2):
        """
        Add a directed edge to the graph.
        """
        try:
            self.vertices[v1].add(v2)
        except:
            print("Invalid vertex.")

    def get_neighbors(self, vertex_id):
        """
        Get all neighbors (edges) of a vertex.
        """
        return self.vertices[vertex_id]

    def bft(self, starting_vertex):
        """
        Print each vertex in breadth-first order
        beginning from starting_vertex.
        """
        #we'll be using a queue for this
        q = Queue()
        #enqueue our start vertex(node)
        q.enqueue(starting_vertex)
        #we need to track visited nodes
        visited = set()

        while q.size() > 0:
            #dequeue. this is our current node
            current_node = q.dequeue()
            if current_node not in visited:
                visited.add(current_node)
                print(current_node)
                neighbors = self.get_neighbors(current_node)
                for neighbor in neighbors:
                    q.enqueue(neighbor)

    def dft(self, starting_vertex):
        """
        Print each vertex in depth-first order
        beginning from starting_vertex.
        """
        #using stack here
        s = Stack()
        #pushing starting vertex onto stack
        s.push(starting_vertex)
        #need to keep track of visited nodes/vertices
        visited = set()

        while s.size() > 0:
            #pop from top. this is our current node
            current_node = s.pop()
            if current_node not in visited:
                visited.add(current_node)
                print(current_node)
                neighbors = self.get_neighbors(current_node)
                for neighbor in neighbors:
                    s.push(neighbor)


    def dft_recursive(self, starting_vertex, visited=None):
        """
        Print each vertex in depth-first order
        beginning from starting_vertex.

        This should be done using recursion.
        """
        #recursion againnn! find base case
        #work towards base case
        #call self

        #base case - is current node in visited?
        #get neighbors and ruin dft_recursive function on them all until we reach base case
        if visited is None:
            visited = set()
        
        current_node = starting_vertex
        neighbors = self.get_neighbors(current_node)

        if current_node not in visited:
            print(current_node)
            visited.add(current_node)
        
            for neighbor in neighbors:
                self.dft_recursive(neighbor, visited)
        return


    def bfs(self, starting_vertex, destination_vertex):
        """
        Return a list containing the shortest path from
        starting_vertex to destination_vertex in
        breath-first order.
        """
        #Queue of paths!
        q = Queue()
        q.enqueue([starting_vertex])
        visited = set()

        while q.size() > 0:
            current_path = q.dequeue()
            #to track visited we need to grab the last vertex of the current path
            current_node = current_path[-1]

            if current_node not in visited:
                visited.add(current_node)
                #is this our target? if so, return the current path
                if current_node == destination_vertex:
                    return current_path
                    
                neighbors = self.get_neighbors(current_node)
                #copy old path
                #append new neighbor
                #enqueue new path
                for neighbor in neighbors:
                    next_path = current_path.copy()
                    next_path.append(neighbor)
                    q.enqueue(next_path)

    def dfs(self, starting_vertex, destination_vertex):
        """
        Return a list containing a path from
        starting_vertex to destination_vertex in
        depth-first order.
        """
        s = Stack()
        s.push([starting_vertex])
        visited = set()

        while s.size() > 0:
            current_path = s.pop()
            current_node = current_path[-1]

            if current_node not in visited:
                visited.add(current_node)
                if current_node == destination_vertex:
                    return current_path
                
                neighbors = self.get_neighbors(current_node)
                for neighbor in neighbors:
                    next_path = current_path.copy()
                    next_path.append(neighbor)
                    s.push(next_path)
                

    def dfs_recursive(self, starting_vertex, destination_vertex, visited=None):
        """
        Return a list containing a path from
        starting_vertex to destination_vertex in
        depth-first order.

        This should be done using recursion.
        """
        if type(starting_vertex) != list:
            starting_vertex = [starting_vertex]

        if visited is None:
            visited = set()

        current_node = starting_vertex[-1]

        if current_node not in visited:
            visited.add(current_node)
            if current_node == destination_vertex:
                return starting_vertex

            neighbors = self.get_neighbors(current_node)

            for neighbor in neighbors:
                if neighbor not in visited:
                    next_path = starting_vertex.copy()
                    next_path.append(neighbor)

                    result = self.dfs_recursive(next_path, destination_vertex, visited)

                    if result is not None:
                        return result
        return None

if __name__ == '__main__':
    graph = Graph()  # Instantiate your graph
    # https://github.com/LambdaSchool/Graphs/blob/master/objectives/breadth-first-search/img/bfs-visit-order.png
    graph.add_vertex(1)
    graph.add_vertex(2)
    graph.add_vertex(3)
    graph.add_vertex(4)
    graph.add_vertex(5)
    graph.add_vertex(6)
    graph.add_vertex(7)
    graph.add_edge(5, 3)
    graph.add_edge(6, 3)
    graph.add_edge(7, 1)
    graph.add_edge(4, 7)
    graph.add_edge(1, 2)
    graph.add_edge(7, 6)
    graph.add_edge(2, 4)
    graph.add_edge(3, 5)
    graph.add_edge(2, 3)
    graph.add_edge(4, 6)

    '''
    Should print:
        {1: {2}, 2: {3, 4}, 3: {5}, 4: {6, 7}, 5: {3}, 6: {3}, 7: {1, 6}}
    '''
    print(graph.vertices)

    '''
    Valid BFT paths:
        1, 2, 3, 4, 5, 6, 7
        1, 2, 3, 4, 5, 7, 6
        1, 2, 3, 4, 6, 7, 5
        1, 2, 3, 4, 6, 5, 7
        1, 2, 3, 4, 7, 6, 5
        1, 2, 3, 4, 7, 5, 6
        1, 2, 4, 3, 5, 6, 7
        1, 2, 4, 3, 5, 7, 6
        1, 2, 4, 3, 6, 7, 5
        1, 2, 4, 3, 6, 5, 7
        1, 2, 4, 3, 7, 6, 5
        1, 2, 4, 3, 7, 5, 6
    '''
    graph.bft(1)

    '''
    Valid DFT paths:
        1, 2, 3, 5, 4, 6, 7
        1, 2, 3, 5, 4, 7, 6
        1, 2, 4, 7, 6, 3, 5
        1, 2, 4, 6, 3, 5, 7
    '''
    graph.dft(1)
    graph.dft_recursive(1)

    '''
    Valid BFS path:
        [1, 2, 4, 6]
    '''
    print(graph.bfs(1, 6))

    '''
    Valid DFS paths:
        [1, 2, 4, 6]
        [1, 2, 4, 7, 6]
    '''
    print(graph.dfs(1, 6))
    print(graph.dfs_recursive(1, 6))
