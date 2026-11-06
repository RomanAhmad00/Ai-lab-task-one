from collections import deque

graph = {
    "A": ["B", "C"],
    "B": ["D", "E"],
    "C": ["F"],
    "D": ["H"],
    "E": ["I"],
    "F": ["G"],
    "G": ["J"],
    "H": [],
    "I": [],
    "J": [],
}

visited = []
queue = deque()

def bfs(node):
    queue.append(node)
    while queue:
        print(list(queue), visited)
        temp = queue.popleft()
        visited.append(temp)
        for child in graph[temp]:
            queue.append(child)

bfs("A")
print(list(queue), visited)
