
from algoritmos.graph import Graph
from search_algorithms import check_consecutivos
from tree import Tree, Node

class Vertice:
    def __init__(self, valor, nivel):
        self.valor = valor
        self.nivel = nivel
        self.lowpt = None
        self.g = None
        self.leaf = True
        self.childs = []


def calcula_lowpt(v, articulacao):
    #verifica a se é articulação
    #v é raiz de T e possui mais de um filho.
    if v.nivel == 0 and len(v.childs) > 0:
        articulacao.append(v)

    #por default consideramos v.lowpt = g.v
    """Se v é uma folha então
        lowpt(v) = g(v).
       Senão
        lowpt(v) = vértice mais próximo à raiz
        dentre g(v) e lowpt(w) para todo filho u
        de v."""
    v.lowpt = v.g
    #caso ele não seja folha, verifica os filhos para saber se algum tem o lowpt menor
    #tbm verifica se ele é articulação
    for c in v.childs:
        if c.lowpt.nivel < v.lowpt.nivel:
            v.lowpt = c.lowpt
        
        #verifica a se é articulação
        """v não é raiz de T e v possui um filho w tal que
            Lowpt(w) = v ou w."""
        if v not in articulacao():
            if c.lowpt == c or c.lowpt == v:
                articulacao.append(v)


def DFS(graph: Graph, tree:Tree, pilha: list, raiz:Node, articulacao) -> Graph:
    
    raiz.g = raiz #define inicialmente o g(v)
    tree.add_vertice(raiz)
    pilha.append(raiz.valor)
   
    for w in graph.neighbors(raiz.valor): 
        
        if w not in tree.vertices():
            #adiciona filho na arvore
            filho = Node(w)
            tree.adicionar_filho(raiz, filho)
            #tree = DFS(graph=graph, tree=tree, pilha=pilha, raiz=w)
            DFS(graph=graph, tree=tree, pilha=pilha, raiz=filho, articulacao=articulacao)

        elif w in pilha and not check_consecutivos(pilha, raiz.valor, w):
            #adiciona aresta de retorno
            node = tree.get_node(w)
            raiz.add_aresta_retorno(node)
            #atualiza 0 valor de g(v)
            raiz.g = node

    calcula_lowpt(raiz, articulacao)
    pilha.remove(raiz)
    return articulacao

