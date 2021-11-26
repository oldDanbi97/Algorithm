from collections import deque

visited = []
need_visited = []
def solution(n, computers):
    answer = 0
    global visited
    global need_visited
    need_visited = [i for i in range(n)]
    graph = dict()
    for i in range(n):
        graph.setdefault(i, [])
    for i in range(n):
        for j in range(n):
            if i != j and computers[i][j] == 1:
                graph[i].append(j)
    while True:
        if len(visited) < n:
            dfs(graph, need_visited[0])
            answer += 1
        else:
            break
    return answer

def dfs(graph, start_node):
    global visited
    global need_visited
    stack = deque()
    stack.append(start_node)
    while stack:
        node = stack.pop()
        if node not in visited:
            visited.append(node)
            need_visited.remove(node)
            stack.extend(reversed(graph[node]))