class Graph:
    def __init__(self):
        self.graph = {}

    def add_vertice(self, vertice):
        if vertice not in self.graph:
            self.graph[vertice] = []

    def add_aresta(self, init, end):
        if init in self.graph:
            self.graph[init].append(end)
        else:
            self.graph[init] = [end]

        if end in self.graph:
            self.graph[end].append(init)
        else:
            self.graph[end] = [init]

    def vertices(self):
        return list(self.graph.keys())

    def arestas(self):
        arestas = []
        for vertice, neighbors in self.graph.items():
            for ngb in neighbors:
                if (ngb, vertice) not in arestas:
                    arestas.append((vertice, ngb))
        return arestas

    def neighbors(self, vertice):
        if vertice in self.graph:
            return self.graph[vertice]
        else:
            return []

    def __str__(self):
        return "Graph: " + str(self.graph)


# Exemplo de uso:
graph = Graph()
graph.add_vertice('A')
graph.add_vertice('B')
graph.add_vertice('C')
graph.add_vertice('D')

graph.add_aresta('A', 'B')
graph.add_aresta('B', 'C')
graph.add_aresta('C', 'D')
graph.add_aresta('D', 'A')

"""
print("Vértices:", graph.vertices())
print("Arestas:", graph.arestas())
print("Vizinhos de B:", graph.neighbors('B'))
print(graph)
"""
