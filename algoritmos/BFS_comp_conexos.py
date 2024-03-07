
from graph import Graph
from search_algorithms import BFS

def find_comp_conex(graph:Graph) -> list:
    
    comp_conexos = [] # (1)
    v_visited = [] # (1)
    graph_result = Graph() # (1)
    for v in graph.vertices(): # (n) número de vertices
        if v not in v_visited: # (n)
            graph_result = BFS(graph=graph, raiz=v) # n(n + m) complexidade da busca em largura
            v_visited.extend(graph_result.vertices()) # (n)
            comp_conexos.append(graph_result) # (n)
           

    return comp_conexos


graph = Graph()
graph.add_vertice('1')
graph.add_vertice('2')
graph.add_vertice('3')
graph.add_vertice('4')
graph.add_vertice('5')
graph.add_vertice('6')
graph.add_vertice('7')
graph.add_vertice('8')
graph.add_vertice('9')

graph.add_aresta('1', '2')
graph.add_aresta('1', '3')
graph.add_aresta('2', '3')
graph.add_aresta('3', '4')
graph.add_aresta('3', '6')
graph.add_aresta('4', '6')
graph.add_aresta('5', '7')
graph.add_aresta('5', '8')
graph.add_aresta('7', '8')
graph.add_aresta('7', '9')
graph.add_aresta('8', '9')


#print("Vértices:", graph.vertices())
# print("Arestas:", graph.arestas())
print("Grafo: ", graph)

comp_conexos = find_comp_conex(graph=graph)
for comp in comp_conexos:
    print("COMPONENTE CONEXO:")
    print(comp)