from collections import deque

graph = {
    'A': ['B', 'C'],
    'B': ['D', 'E'],
    'C': ['F'],
    'D': [],
    'E': ['F'],
    'F': []
}

def bfs(graph, start):
    visited = []
    queue = deque([start]) 

    while queue:
        node = queue.popleft()
        if node not in visited:
            visited.append(node)
            neighbors = graph[node]
            for neighbor in neighbors:
                queue.append(neighbor)

    return visited

start_node = 'A'
result = bfs(graph, start_node)

print(result)