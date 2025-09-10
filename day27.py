from collections import deque

def shortest_path(v, edges, s, e):
    g = [[] for _ in range(v)]
    for x, y in edges:
        g[x].append(y)
        g[y].append(x)
    q = deque([(s, 0)])
    vis = [0] * v
    vis[s] = 1
    while q:
        u, d = q.popleft()
        if u == e:
            return d
        for nei in g[u]:
            if not vis[nei]:
                vis[nei] = 1
                q.append((nei, d + 1))
    return -1


v = int(input())
e = int(input())
edges = []
for _ in range(e):
    x, y = map(int, input().split())
    edges.append([x, y])
s, e = map(int, input().split())

print(shortest_path(v, edges, s, e))
