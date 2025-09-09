
 from collections import defaultdict

def has_cycle(n, edges):
    g = defaultdict(list)
    for a, b in edges:
        g[a].append(b)
        g[b].append(a)

    vis = [False] * n

    def dfs(u, p):
        vis[u] = True
        for v in g[u]:
            if not vis[v]:
                if dfs(v, u):
                    return True
            elif v != p:
                return True
        return False

    for i in range(n):
        if not vis[i]:
            if dfs(i, -1):
                return True
    return False


print(has_cycle(5, [[0,1],[1,2],[2,3],[3,4],[4,0]]))
print(has_cycle(3, [[0,1],[1,2]]))
