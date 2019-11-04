"""
Simple graph implementation
"""
from util import Stack, Queue  # These may come in handy

class Graph:
    """Represent a graph as a dictionary of vertices mapping labels to edges."""
    def __init__(self):
        self.vertices = {}
        
    def add_vertex(self, vertex):
        """
        Add a vertex to the graph.
        """
        self.vertices[vertex] = set()
        
    def add_edge(self, v1, v2):
        """
        Add a directed edge to the graph.
        """
        if v1 in self.vertices and v2 in self.vertices:
            self.vertices[v1].add(v2)
        else:
            raise IndexError("That vertex does not exist.")
        
    def bft(self, starting_vertex):
        """
        Print each vertex in breadth-first order
        beginning from starting_vertex.
        """
        # Create an empty queue and enqueue the starting vertex ID
        q = Queue()
        q.enqueue(starting_vertex)
        # Create an empty Set to store visited vertices
        visited = set()
        # While the queue is not empty...
        while q.size() > 0:
            # Dequeue the first vertex
            v = q.dequeue()
            # If that vertex has not been visited...
            if v not in visited:
                # Mark it as visited
                print(v)
                visited.add(v)
                # Then add all of its neighbors to the back of the queue
                for neighbor in self.vertices[v]:
                    q.enqueue(neighbor)
                    
    def dft(self, starting_vertex):
        """
        Print each vertex in depth-first order
        beginning from starting_vertex.
        """
        # Create an empty stack and push the starting vertex ID
        s = Stack()
        s.push(starting_vertex)
        # Create a Set to store visited vertices
        visited = set()
        # While the stack is not empty...
        while s.size() > 0:
            # Pop the first vertex
            v = s.pop()
            # If that vertex has not been visited...
            if v not in visited:
                # Mark it as visited...
                print(v)
                visited.add(v)
                # Then add all of its neighbors to the top of the stack
                for neighbor in self.vertices[v]:
                    s.push(neighbor)
                    

    def dft_recursive(self, starting_vertex, visited=None):
        """
        Print each vertex in depth-first order
        beginning from starting_vertex.
        This should be done using recursion.
        """
        # 
        if visited is None:
            # Create a Set to store visited vertices on initial call
            visited = set()
        # add the current vertex to the visited set and print it out
        visited.add(starting_vertex)
        print(starting_vertex)
        # Loop through the set at current key
        for neighbor in self.vertices[starting_vertex]:
            # if current value in set hasn't been visited
            if neighbor not in visited:
                # call recursively with current value and visited set 
                # NOTE a return statement here will terminate the recursion early as we are not
                # returning the value but rather building the set of visited vertices
                self.dft_recursive(neighbor, visited)
    
    def bfs(self, starting_vertex, destination_vertex):
        """
        Return a list containing the shortest path from
        starting_vertex to destination_vertex in
        breath-first order.
        """
        # Create an empty queue and enqueue A PATH TO the starting vertex ID
        queue = Queue()
        if type(starting_vertex) == int:
            starting_vertex = [starting_vertex]
        queue.enqueue(starting_vertex)
        # print(f"starting vertex {starting_vertex}")
        # Create a Set to store visited vertices
        visited = set()
        # While the queue is not empty...
        while queue.size() > 0:
            # Dequeue the first PATH
            v = queue.dequeue()
            # Grab the last vertex from the PATH
            potential_target = v[-1]
            # print(f"potential target {potential_target}, visited: {visited}, destination: {destination_vertex}")
            # If that vertex has not been visited...
            if potential_target not in visited:
                # CHECK IF IT'S THE TARGET
                if potential_target == destination_vertex:
                    # print(f"found vertex via {visited}")
                    # IF SO, RETURN PATH
                    return v
                # Mark it as visited...
                visited.add(potential_target)
                # Then add A PATH TO its neighbors to the back of the queue
                for neighbor in self.vertices[potential_target]:
                    # COPY THE PATH
                    new_path = v[:]
                    new_path.append(neighbor)
                    # APPEND THE NEIGHBOR TO THE BACK
                    queue.enqueue(new_path)
                    
    def dfs(self, starting_vertex, destination_vertex):
        """
        Return a list containing a path from
        starting_vertex to destination_vertex in
        depth-first order.
        """
        stack = Stack()
        if type(starting_vertex) == int:
            starting_vertex = [starting_vertex]
        stack.push(starting_vertex)
        # print(f"starting vertex {starting_vertex}")
        # Create a Set to store visited vertices
        visited = set()
        # While the queue is not empty...
        while stack.size() > 0:
            # Dequeue the first PATH
            v = stack.pop()
            # Grab the last vertex from the PATH
            potential_target = v[-1]
            # print(f"potential target {potential_target}, visited: {visited}, destination: {destination_vertex}")
            # If that vertex has not been visited...
            if potential_target not in visited:
                # CHECK IF IT'S THE TARGET
                if potential_target == destination_vertex:
                    # print(f"found vertex via {visited}")
                    # IF SO, RETURN PATH
                    return v
                # Mark it as visited...
                visited.add(potential_target)
                # Then add A PATH TO its neighbors to the back of the queue
                for neighbor in self.vertices[potential_target]:
                    # COPY THE PATH
                    new_path = v[:]
                    new_path.append(neighbor)
                    # APPEND THE NEIGHBOR TO THE BACK
                    stack.push(new_path)
    




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
    print('\n==============\n')
    
    '''
    Valid DFT paths:
        1, 2, 3, 5, 4, 6, 7
        1, 2, 3, 5, 4, 7, 6
        1, 2, 4, 7, 6, 3, 5
        1, 2, 4, 6, 3, 5, 7
    '''
    graph.dft(1)
    print('\n==============\n')
    
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
    print('\n==============\n')
    
    '''
    Valid DFT recursive paths:
        1, 2, 3, 5, 4, 6, 7
        1, 2, 3, 5, 4, 7, 6
        1, 2, 4, 7, 6, 3, 5
        1, 2, 4, 6, 3, 5, 7
    '''
    graph.dft_recursive(1)
    print('\n==============\n')
    
    '''
    Valid BFS path:
        [1, 2, 4, 6]
    '''
    print(graph.bfs(1, 6))
    print('\n==============\n')
    
    '''
    Valid DFS paths:
        [1, 2, 4, 6]
        [1, 2, 4, 7, 6]
    '''
    print(graph.dfs(1, 6))
    print('\n==============\n')