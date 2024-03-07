from graph import Graph
from collections import deque

def BFS(graph:Graph, raiz) -> Graph:
    graph_result = Graph() # (1)
    fila = deque() # (1)
    fila.append(raiz) # (1)
    graph_result.add_vertice(raiz) # (1)
    while len(fila) != 0: # (n) número de vertices
        v = fila.popleft() (1) # (n)
        for w in graph.neighbors(v): # (d(u)) grau de adjacência do vértice
            if w not in graph_result.vertices(): # (n)
                fila.append(w) # (n)
                graph_result.add_vertice(w) # (n)
                graph_result.add_aresta(v,w) # (n)
            elif (v,w) not in graph_result.arestas(): # (n)
                graph_result.add_aresta(v,w) # (n)
    
    return graph_result
