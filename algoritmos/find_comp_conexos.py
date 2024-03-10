

def verifica_demarcadores(v):
    pai = v.pai
    if v.lowpt == pai or v.lowpt == v:
            return True
            

def DFS(graph: Graph, tree:Tree, pilha: list, raiz:Node, articulacao) -> Graph:
    
    raiz.g = raiz #define inicialmente o g(v)
    tree.add_vertice(raiz)
    pilha.append(raiz.valor)
    comp_conexas = []

   
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
        if verifica_demarcadores(raiz):
            comp.append(raiz.pai)
            for filho in raiz.filhos():
                comp.append(filho)
                tree.remove(filho)
            tree.remove(raiz)
            comp_conexas.append(comp)

             #componente biconaxa com filhos de raiz