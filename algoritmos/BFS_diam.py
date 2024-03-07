from graph import Graph
from collections import deque

#bfs modificado para realizar o calculo da exentricidade em relação a um vétice do grafo

def BFS(graph:Graph, raiz) -> Graph:
    
    graph_result = Graph()
    max_dist = (raiz, 0)
    fila = deque([max_dist]) 
    graph_result.add_vertice(raiz)
    
    while len(fila) != 0: 
        v, dist = fila.popleft() 
        #print("dist", dist)
        
        if dist > max_dist[1]:  
            max_dist = (v, dist)
            #print("DISTANCIA", raiz, max_dist)
        
        for w in graph.neighbors(v):
            if w not in graph_result.vertices(): # (n)
                #print("vizinho", w)
                fila.append((w, dist + 1)) 
                graph_result.add_vertice(w) 
                graph_result.add_aresta(v,w)

            elif (v,w) not in graph_result.arestas():
                graph_result.add_aresta(v,w) 
        
    
    return max_dist


def diam_calc(graph:Graph):

    vertice_init = graph.vertices()[0] #inicializa vertices de inicio e fim
    vertice_end = graph.vertices()[0]
    
    diam = 0 #inicializa diametro
    
    for v in graph.vertices():
        
        v_dist, diam_result = BFS(graph=graph, raiz=v)
        
        if(diam_result > diam):
            vertice_init = v
            vertice_end = v_dist
            diam = diam_result

    return (vertice_init, vertice_end, diam)



graph = Graph()
graph.add_vertice('1')
graph.add_vertice('2')
graph.add_vertice('3')
graph.add_vertice('4')
graph.add_vertice('5')
graph.add_vertice('6')
graph.add_vertice('7')
graph.add_vertice('8')

graph.add_aresta('1', '7')
graph.add_aresta('1', '4')
graph.add_aresta('2', '7')
graph.add_aresta('3', '8')
graph.add_aresta('3', '4')
graph.add_aresta('3', '5')
graph.add_aresta('4', '6')
graph.add_aresta('4', '5')
graph.add_aresta('5', '6')



#print("Vértices:", graph.vertices())
#print("Arestas:", graph.arestas())
print("Grafo: ", graph)

diametro = diam_calc(graph=graph)
print("DIAMETRO:")
print(diametro)
    





    