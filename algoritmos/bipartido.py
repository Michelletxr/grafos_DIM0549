
class Vertice:
    def __init__(self, valor, ):
        self.valor = valor
        self.cor = None



def bipartido_dfs(self, vertice, cor):
        vertice.cor = cor
        for vizinho in self.grafo[vertice]:
            if not vizinho.cor:
                if not self.bipartido_dfs(vizinho, 1 - cor):
                    return False
            elif vizinho.cor == cor:
                return False
        return True

def bipartido(self):
        for vertice in range(self.vertices):
            if vertice not in self.cores:
                if not self.bipartido_dfs(vertice, 0):
                    return False
        return True