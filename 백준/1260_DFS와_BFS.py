import sys
from collections import deque

def dfs(graph, V, visited=[]):
    visited.append(V)
    for node in sorted(graph[V]):
        if node not in visited:
            dfs(graph, node, visited)
    return visited

def bfs(graph, V):
    visited = []
    queue = deque([V])
    while queue:
        node = queue.popleft()
        if node not in visited:
            visited.append(node)
            queue.extend(sorted(graph[node]))
    return visited

read = sys.stdin.readline
N, M, V = list(map(int, read().strip().split()))
graph = dict()

for i in range(1, N+1):
    graph[i] = []
for _ in range(M):
    a, b = list(map(int, read().strip().split()))
    graph[a].append(b)
    if a not in graph[b]:
        graph[b].append(a)
for i in dfs(graph, V):
    print(i, end=' ')
print()
for i in bfs(graph, V):
    print(i, end=' ')