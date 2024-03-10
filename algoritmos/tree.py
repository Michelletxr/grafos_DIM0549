
class Node:
    def __init__(self, valor):
        self.valor = valor
        self.nivel = 0
        self.lowpt = None
        self.g = None
        self.childs = []


class Tree:
    def __init__(self, raiz=None):
        self.raiz = raiz
        self.vertices = set()

    def adicionar_filho(self, pai, filho): 
        if pai is None:
            self.raiz = filho
        else:
            filho.nivel = pai.nivel + 1
            pai.childs.append(filho)
        
    def add_vertice(self, pai, filho):
        self.vertices.append(filho.valor)

    def imprimir_arvore(self, no=None, nivel=0):
        if no is None:
            no = self.raiz

        print(" " * nivel + str(no.valor))
        for filho in no.childs:
            self.imprimir_arvore(filho, nivel + 1)


# Exemplo de uso:
if __name__ == "__main__":
    # Construindo uma árvore
    raiz = Node(1)
    filho1 = Node(2)
    filho2 = Node(3)
    neto1 = Node(4)
    neto2 = Node(5)
    neto3 = Node(6)

    arvore = Tree(raiz)
    arvore.adicionar_filho(raiz, filho1)
    arvore.adicionar_filho(raiz, filho2)
    arvore.adicionar_filho(filho1, neto1)
    arvore.adicionar_filho(filho1, neto2)
    arvore.adicionar_filho(filho2, neto3)

    # Imprimindo a árvore
    arvore.imprimir_arvore()