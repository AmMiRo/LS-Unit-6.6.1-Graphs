"""
Simple graph implementation
"""
from util import Stack, Queue  # These may come in handy

class Graph:

    """Represent a graph as a dictionary of vertices mapping labels to edges."""
    def __init__(self):
        self.vertices = {}

    def add_vertex(self, vertex_id):
        # Add a vertex to the graph.

        self.vertices[vertex_id] = set()

    def add_edge(self, v1, v2):
        # Add a directed edge to the graph.

        if v1 not in self.vertices:
            print(f"Error: {v1} is not a valid vertex")
        elif v2 not in self.vertices:
            print(f"Error: {v2} is not a valid vertex")
        else:
            self.vertices[v1].add(v2)

    def get_neighbors(self, vertex_id):
        # Get all neighbors (edges) of a vertex.

        return self.vertices[vertex_id]

    def bft(self, starting_vertex):
        # Print each vertex in breadth-first order beginning from starting_vertex.

        queue = Queue()
        queue.enqueue(starting_vertex)
        visited_verts = set([starting_vertex])
        while queue.size() > 0:
            curr_vert = queue.dequeue()
            neighbors = self.get_neighbors(curr_vert)
            for neighbor in neighbors:
                if neighbor not in visited_verts:
                    visited_verts.add(neighbor)
                    queue.enqueue(neighbor)
            print(curr_vert)

    def dft(self, starting_vertex):
        # Print each vertex in depth-first order beginning from starting_vertex.

        stack = Stack()
        stack.push(starting_vertex)
        visited_verts = set([starting_vertex])
        while stack.size() > 0:
            curr_vert = stack.pop()
            neighbors = self.get_neighbors(curr_vert)
            for neighbor in neighbors:
                if neighbor not in visited_verts:
                    visited_verts.add(neighbor)
                    stack.push(neighbor)
            print(curr_vert)

    def dft_recursive(self, starting_vertex, visited_verts=None):
        # Print each vertex in depth-first order beginning from starting_vertex.

        # This should be done using recursion.
        
        if visited_verts is None:
            visited_verts = set([starting_vertex])
        print(starting_vertex)
        neighbors = self.get_neighbors(starting_vertex)
        for neighbor in neighbors:
            if neighbor not in visited_verts:
                visited_verts.add(neighbor)
                self.dft_recursive(neighbor, visited_verts)

    def bfs(self, starting_vertex, destination_vertex):
        # Return a list containing the shortest path from starting_vertex to destination_vertex in breath-first order.

        queue = Queue()
        queue.enqueue(starting_vertex)
        visited_verts = {starting_vertex: None}
        while queue.size() > 0:
            curr_vert = queue.dequeue()
            neighbors = self.get_neighbors(curr_vert)
            for neighbor in neighbors:
                if neighbor == destination_vertex:
                    result = [neighbor]
                    vert = curr_vert
                    while vert is not None:
                        result.insert(0, vert)
                        vert = visited_verts[vert]
                    return result
                else:
                    if neighbor not in visited_verts:
                        visited_verts[neighbor] = curr_vert
                        queue.enqueue(neighbor)


    def dfs(self, starting_vertex, destination_vertex):
        # Return a list containing a path from starting_vertex to destination_vertex in depth-first order.

        stack = Stack()
        stack.push(starting_vertex)
        visited_verts = {starting_vertex: None}
        while stack.size() > 0:
            curr_vert = stack.pop()
            neighbors = self.get_neighbors(curr_vert)
            for neighbor in neighbors:
                if neighbor == destination_vertex:
                    result = [neighbor]
                    vert = curr_vert
                    while vert is not None:
                        result.insert(0, vert)
                        vert = visited_verts[vert]
                    return result
                else:
                    if neighbor not in visited_verts:
                        visited_verts[neighbor] = curr_vert
                        stack.push(neighbor)
        

    def dfs_recursive(self, starting_vertex, destination_vertex, visited_verts=None):
        # Return a list containing a path from starting_vertex to destination_vertex in depth-first order.

        # This should be done using recursion.

        if visited_verts is None:
            visited_verts = set([starting_vertex])
        neighbors = self.get_neighbors(starting_vertex)
        if starting_vertex == destination_vertex:
            return [starting_vertex]
        for neighbor in neighbors:
            if neighbor not in visited_verts:
                visited_verts.add(neighbor)
                lst = self.dfs_recursive(neighbor, destination_vertex, visited_verts)
                if lst is not None:
                    return [starting_vertex] + lst
        

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
