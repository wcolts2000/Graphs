# Write a function that takes a 2d binary array and 
# returns the number of 1 islands. An island consists
# of 1s that are connected to the north, south, east or west

# For example

# Unweighted
# Undirected
# Cyclic

# Nodes are numbers, edges are connections between 1s

islands = [[0, 1, 0, 1, 0],
           [1, 1, 0, 1, 1],
           [0, 0, 1, 0, 0],
           [1, 0, 1, 0, 0],
           [1, 1, 0, 0, 0]]

# Visit each cell in the 2d array
# When you come across a 1, traverse it and mark all connected nodes as visited
# then increment a counter

class Stack():
    def __init__(self):
        self.stack = []
    def push(self, value):
        self.stack.append(value)
    def pop(self):
        if self.size() > 0:
            return self.stack.pop()
        else:
            return None
    def size(self):
        return len(self.stack)

def get_island_neighbors(x, y, matrix):
    neighbors = []
    # Check if there is a 1 to the north
    if y > 0 and matrix[y - 1][x] == 1:
        neighbors.append( (x, y-1) )
    # Check if there is a 1 to the south
    if y < len(matrix) - 1 and matrix[y + 1][x] == 1:
        neighbors.append( (x, y+1) )
    # Check if there is a 1 to the east
    if x < len(matrix[0]) - 1 and matrix[y][x + 1] == 1:
        neighbors.append( (x + 1, y) )
    # Check if there is a 1 to the west
    if x > 0 and matrix[y][x - 1] == 1:
        neighbors.append((x - 1, y))
    return neighbors


def dft_islands(start_x, start_y, matrix, visited):
    '''
    Returns an updated visited matrix after a dft of matrix starting from x, y
    '''
    s = Stack()
    s.push((start_x,start_y))
    while s.size() > 0:
        v = s.pop()
        x = v[0]
        y = v[1]

        if not visited[y][x]:
            visited[y][x] = True
            for neighbor in get_island_neighbors(x, y, matrix):
                s.push(neighbor)
    return visited

def island_counter(matrix):
    # create a visited matrix with the same dimensions as the islands matrix
    visited = []
    matrix_height = len(matrix)
    matrix_width = len(matrix[0])
    for i in range(matrix_height):
        visited.append([False] * matrix_width)
    counter = 0
    # For each each cell in the 2d array
    for x in range(matrix_width):
        for y in range(matrix_height):
            # If it has not been visited...
            # when you come across a 1,
            if not visited[y][x]:
                # traverse it and mark all connected 
                # nodes as visited,
                if matrix[y][x] == 1:
                    visited = dft_islands(x, y, matrix, visited) # STUB
                    # then increment a counter
                    counter += 1
    return counter


big_islands = [[1, 0, 0, 1, 1, 0, 1, 1, 0, 1],
               [0, 0, 1, 1, 0, 1, 0, 0, 0, 0],
               [0, 1, 1, 1, 0, 0, 0, 1, 0, 1],
               [0, 0, 1, 0, 0, 1, 0, 0, 1, 1],
               [0, 0, 1, 1, 0, 1, 0, 1, 1, 0],
               [0, 1, 0, 1, 1, 1, 0, 1, 0, 0],
               [0, 0, 1, 0, 0, 1, 1, 0, 0, 0],
               [1, 0, 1, 1, 0, 0, 0, 1, 1, 0],
               [0, 1, 1, 0, 0, 0, 1, 1, 0, 0],
               [0, 0, 1, 1, 0, 1, 0, 0, 1, 0]] 
               
print(island_counter(big_islands))  # 13 
 
 
 
 
 
 

print(island_counter(islands)) # returns 4 
 
