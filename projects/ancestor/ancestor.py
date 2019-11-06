# DFS ATTEMPT
# class Stack():
#     def __init__(self):
#         self.stack = []
#     def push(self, value):
#         self.stack.append(value)
#     def pop(self):
#         if self.size() > 0:
#             return self.stack.pop()
#         else:
#             return None
#     def size(self):
#         return len(self.stack)

# test_ancestors = [(1, 3), (2, 3), (3, 6), (5, 6), (5, 7), (4, 5), (4, 8), (8, 9), (11, 8), (10, 1)]

# class Graph:
#     """
#     Represent a graph as a dictionary of child to parent relationships mapping children to parents.
#     """
#     def __init__(self):
#         self.family_tree = {}
        
#     def add_child(self, child):
#         """
#         Add a child to the graph.
#         """
#         self.family_tree[child] = set()
        
#     def add_parent(self, child, parent):
#         """
#         Add a directed parent to the graph.
#         """
#         if child in self.family_tree:
#             # print(f"current set: {self.family_tree[child]}")
#             self.family_tree[child].add(parent)
#             # print(f"current set after: {self.family_tree[child]}")
#         else:
#             raise IndexError("That parent does not exist.")

#     def dft(self, child):
#         """
#         Print each vertex in depth-first order
#         beginning from child.
#         """
#         # Create an empty stack and push the starting vertex ID
#         stack = Stack()
#         stack.push([[child, 0]])
#         # Create a Set to store visited family_tree
#         visited = list()
#         # While the stack is not empty...
#         while stack.size() > 0:
#             # Pop the first vertex
#             current_child_path = stack.pop()
#             current_child = current_child_path[-1][0]
#             print(f"Cirrent {current_child}")
#             # If that vertex has not been visited...
#             if current_child not in visited:
#                 # Mark it as visited...
#                 # print(current_child)
#                 visited.append(current_child)
#                 # Then add all of its neighbors to the top of the stack
                
#                 if current_child in self.family_tree:
#                     for parent in self.family_tree[current_child]:
#                         new_path = current_child_path[:]
#                         new_path.append(parent)
#                         stack.push(new_path)
#         print(f"visited: {visited}")
#         if len(visited) > 1:
#             if len(visited) == 3:
#                 if visited[1] > visited[-1]:
#                     return visited[-1]
#                 else:
#                     return visited[1]
#             else:
#                 return visited[-1]
#         else:
#             return -1

# def earliest_ancestor(ancestors, starting_node):
#     # build a hashtable from ancestors with the key being the parent and the value being the child
#     ht = Graph()
#     # add child nodes
#     for pair in ancestors:
#         ht.add_child(pair[1])
#         # add parent nodes
#     for pair in ancestors:
#         ht.add_parent(pair[1], pair[0])
#     # print(f"ht: {ht.family_tree}")
#     return ht.dft(starting_node)
#     # build a helper method to check the value (child) and see if there are any 
#     # keys (parents) that correspond to it, tracking a number of steps from the target child node
#     # loop until farthest parent has been found

    

# print(earliest_ancestor(test_ancestors, 6))

# BFS SOLUTION

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
    """Represent a graph as a dictionary of vertices mapping labels to edges."""
    def __init__(self):
        self.vertices = {}
    def add_vertex(self, vertex_id):
        if vertex_id not in self.vertices:
            self.vertices[vertex_id] = set()
    def add_edge(self, v1, v2):
        if v1 in self.vertices and v2 in self.vertices:
            self.vertices[v1].add(v2)
        else:
            raise IndexError("That vertex does not exist!")


def earliest_ancestor(ancestors, starting_node):
    # Build the graph
    graph = Graph()
    for pair in ancestors:
        graph.add_vertex(pair[0])
        graph.add_vertex(pair[1])
        # Build edges in reverse
        graph.add_edge(pair[1], pair[0])
    # Do a BFS (storing the path)
    queue = Queue()
    queue.enqueue([starting_node])
    # a place to store the longest path variable
    longest_branch = 1
    # a place to store the return answer
    earliest_ancestor = -1
    # while there are still nodes in queue:
    while queue.size() > 0:
        # remove first element from queue
        family_tree = queue.dequeue()
        # grab the last item in the list (the current node)
        current_node = family_tree[-1]
        current_size = len(family_tree)
        # If the family_tree is longer or equal and the value is smaller, or if the family_tree is longer)
        if (current_size >= longest_branch and current_node < earliest_ancestor) or (current_size > longest_branch):
            # update earliest to current node
            earliest_ancestor = current_node
            # and update longest branch to the size of current family tree branch
            longest_branch = current_size
        # traverse the parents
        for parent in graph.vertices[current_node]:
            # copy the family tree
            family_tree_copy = family_tree[:]
            # add current node the family tree
            family_tree_copy.append(parent)
            # add family tree copy to queue
            queue.enqueue(family_tree_copy)
    # return the earliest ancestor
    return earliest_ancestor