# Lab 3 - DFS (Depth First Search)
# Sir ne class mein is tarah karwaya tha: stack se, har step par
# stack aur visited print hota hai.
# Graph wahi hai jo Sir ne class mein likha tha, bas nodes thore
# zyada kar diye hain: H, I aur J add kiye hain.

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
