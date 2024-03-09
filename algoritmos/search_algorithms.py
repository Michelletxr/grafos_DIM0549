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

def check_consecutivos(lista, elemento1, elemento2):
    #print("pilha", lista)
    # Verifica se os elementos estão na lista
    if elemento1 in lista and elemento2 in lista:
        # Obtém os índices dos elementos na lista
        indice1 = lista.index(elemento1)
        indice2 = lista.index(elemento2)
        # Verifica se os índices são consecutivos
        if abs(indice1 - indice2) == 1:
            return True
    return False



def DFS(graph: Graph, tree, pilha: list, raiz) -> Graph:
    tree.add_vertice(raiz)
    pilha.append(raiz)
    #print("|--", raiz)
    for w in graph.neighbors(raiz):
        if w not in tree.vertices():
            tree.add_vertice(w)
            tree.add_aresta(raiz, w)
            #print("adicionando aresta:", (raiz,w))
            tree = DFS(graph=graph, tree=tree, pilha=pilha, raiz=w)
        elif w in pilha and not check_consecutivos(pilha, raiz, w):
            #aresta de retorno
            #print("adicionando aresta de retorno:", (raiz, w))
            tree.add_aresta(raiz, w)
    pilha.remove(raiz)
    return tree
