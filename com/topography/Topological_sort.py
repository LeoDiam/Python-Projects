g = {
    0: [1, 3],
    1: [2],
    2: [],
    3: [4],
    4: [2, 5],
    5: [],
    6: [3, 7],
    7: [],
    8: [6, 9],
    9: [7],
    10: []
}


def dfs(g, node, positions, visited):
    visited[node] = True
    for v in g[node]:
        if not visited[v]:
            dfs(g, v, positions, visited)
    positions.insert(0, node)


def topological_sort(g):
    positions = []
    visited = [False] * len(g)

    num_nodes = len(g)

    for i in range(num_nodes):
        if not visited[i]:
            dfs(g, i, positions, visited)

    return positions
print(topological_sort(g))