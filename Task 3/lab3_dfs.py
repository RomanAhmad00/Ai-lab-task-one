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
stack = []

def dfs(node):
    stack.append(node)
    while stack:
        print(stack, visited)
        temp = stack.pop()
        visited.append(temp)
        for child in graph[temp]:
            stack.append(child)

dfs("A")
print(stack, visited)
