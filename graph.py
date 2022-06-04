import random

class Vertex():
    def __init__(self, value) -> None:
        self.value = value
        self.neighbors = {} #maps neighbor vertex to weight
        self.list_neighbors = []
        self.list_weights = []
    
    def increment_edge(self, vertex, val = 1):
        self.neighbors[vertex] = self.neighbors.get(vertex, 0) + val

    def generate_probability_maps(self):
        for (vertex, weight) in self.neighbors.items():
            self.list_neighbors.append(vertex)
            self.list_weights.append(weight)

    def get_next(self):
        return random.choices(self.list_neighbors, self.list_weights)[0]

class Graph:
    def __init__(self) -> None:
        self.vertices = {} #map value to vertex

    def get_all_val(self):
        return set(self.vertices.keys())
    
    def add_vertex(self, val):
        #so as to not overrwrite existing value
        if val not in self.vertices.keys():
            self.vertices[val] = Vertex(val)
    
    def get_vertex(self, val):
        self.add_vertex(val)
        return self.vertices[val]

    def get_next_word(self, curr):
        return self.vertices[curr.value].get_next()

    def generate_probability_maps(self):
        for vertex in self.vertices.values():
            vertex.generate_probability_maps()