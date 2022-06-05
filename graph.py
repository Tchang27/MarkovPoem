import random


class Vertex():
    '''
    Vertex: represents a word in a Markov Chain
    '''
    def __init__(self, value) -> None:
        '''
        Constructor for Vertex
        '''
        self.value = value
        self.neighbors = {} #maps neighbor vertex to weight
        self.list_neighbors = []
        self.list_weights = []
    
    def increment_edge(self, vertex, val = 1):
        '''
        Function that increments an edge weight

        Parameters:
        vertex - neighbor vertex to increment
        val - increment weight value, default value 1
        '''
        self.neighbors[vertex] = self.neighbors.get(vertex, 0) + val

    def generate_probability_maps(self):
        '''
        Function that generates probability mappings used to get the next word
        '''
        for (vertex, weight) in self.neighbors.items():
            self.list_neighbors.append(vertex)
            self.list_weights.append(weight)

    def get_next(self):
        '''
        Function that retrieves next word based off probability mappings
        '''
        return random.choices(self.list_neighbors, self.list_weights)[0]

class Graph:
    '''
    Graph - rpresentation of the Markov Chain
    '''
    def __init__(self) -> None:
        '''
        Constructor for Graph
        '''
        self.vertices = {} #map value to vertex

    def get_all_val(self):
        '''
        Function that returns all values (words)

        Returns:
        A set of all words in the chain
        '''
        return set(self.vertices.keys())
    
    def add_vertex(self, val):
        '''
        Function that adds a vertex to the chain

        Parameters:
        val - string of the word to be added to the chain
        '''
        #so as to not overrwrite existing value
        if val not in self.vertices.keys():
            self.vertices[val] = Vertex(val)
    
    def get_vertex(self, val):
        '''
        Function that retrieves a vertex if it exists, adds it if not

        Parameters:
        val - word to be retrieved

        Returns:
        Vertex object
        '''
        self.add_vertex(val)
        return self.vertices[val]

    def get_next_word(self, curr):
        '''
        Function that gets the next word in the chain

        Parameter:
        curr - current vertex

        Returns:
        Vertex object
        '''

        return self.vertices[curr.value].get_next()

    def generate_probability_maps(self):
        '''
        Function that generates probability mappings for each vertex
        '''
        for vertex in self.vertices.values():
            vertex.generate_probability_maps()