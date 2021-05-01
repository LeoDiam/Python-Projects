g = {
    0: [1, 2, 3],
    1: [0, 4],
    2: [0, 4],
    3: [0, 5],
    4: [5],
    5: [4, 6, 7],
    6: [],
    7: []
}
visited = [False] * len(g)


def dfs(g, node):
    print("Visiting", node)
    visited[node] = True
    for v in g[node]:
        if not visited[v]:
            dfs(g, v)


dfs(g, 0)
print(g[0][0])

# def dfs_stack(g, node):
#     s = []
#     visited = [ False ] * len(g)
#
#     s.append(node)
#     while len(s) != 0:
#         print("Stack", s)
#         c = s.pop()
#         print("Visiting", c)
#         visited[c] = True
#         for v in g[c]:
#             if not visited[v]:
#                 s.append(v)
#     return visited
#
# dfs_stack(g, 0)

#solution in order to not appear twice
# def dfs_nd_stack(g, node):
#     s = []
#     visited = [False] * len(g)
#     instack = [False] * len(g)
#
#     s.append(node)
#     instack[node] = True
#     while len(s) != 0:
#         print("Stack", s)
#         c = s.pop()
#         instack[c] = False
#         print("Visiting", c)
#         visited[c] = True
#         for v in g[c]:
#             if not visited[v] and not instack[v]:
#                 s.append(v)
#                 instack[v] = True
#     return visited
#
#
# dfs_nd_stack(g2, 0)