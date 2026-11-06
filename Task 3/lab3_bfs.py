# Lab 3 - BFS (Breadth First Search)
# Sir ke DFS wale style mein, bas stack ki jagah queue hai.
# Graph wahi hai jo Sir ne class mein likha tha, bas nodes thore
# zyada kar diye hain: H, I aur J add kiye hain.

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
