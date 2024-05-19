def warshall(graph):
    n = len(graph)
    closure = [[0] * n for _ in range(n)]

    # Inicializa a matriz de fecho transitivo com as conexões diretas do grafo
    for i in range(n):
        for j in range(n):
            closure[i][j] = graph[i][j]

    # Executa o algoritmo de Warshall
    for k in range(n):
        for i in range(n):
            for j in range(n):
                closure[i][j] = closure[i][j] or (closure[i][k] and closure[k][j])

    return closure

# Matriz de adjacência do grafo
graph = [
    [0, 1, 1, 1],
    [0, 0, 1, 1],
    [0, 0, 0, 1],
    [0, 0, 0, 0]
]

# Aplica o algoritmo de Warshall
transitive_closure = warshall(graph)

# Saída do fecho transitivo do grafo
print("Fecho Transitivo do Grafo:")
for row in transitive_closure:
    print(row)
