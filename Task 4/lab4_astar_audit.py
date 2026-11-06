import heapq

graph = {"S": [("A", 1), ("B", 4)], "A": [("C", 2)],
         "B": [("G", 5)], "C": [("G", 3)], "G": []}

h = {"S": 5, "A": 4, "B": 4, "C": 2, "G": 0}


def astar(graph, h, start, goal, show=True):
    pq = [(h[start], 0, start, [start])]
    best = {start: 0}
    expanded = []
    while pq:
        if show:
            print("Open:", sorted([(ff, nn) for ff, gg, nn, pp in pq]))
            print("Closed:", expanded)
        f, g, node, path = heapq.heappop(pq)
        if node == goal:
            if show:
                print("goal", node, "| g:", g, "| path:", path, "(not counted as expanded)")
            return g, path, expanded
        if g != best[node]:
            if show:
                print("skip stale entry:", node, "g:", g)
            continue
        expanded.append(node)
        for nxt, w in graph.get(node, []):
            ng = g + w
            if ng < best.get(nxt, float("inf")):
                best[nxt] = ng
                heapq.heappush(pq, (ng + h[nxt], ng, nxt, path + [nxt]))
        if show:
            print("expand", node, "| g:", g, "| h:", h[node], "| f:", f,
                  "| frontier:", sorted([(ff, nn) for ff, gg, nn, pp in pq]))
    return None, None, expanded


def path_cost(path):
    total = 0
    for i in range(len(path) - 1):
        for nxt, w in graph[path[i]]:
            if nxt == path[i + 1]:
                total += w
    return total


def true_costs(graph, goal):
    zero = {n: 0 for n in graph}
    costs = {}
    for node in graph:
        cost, path, _ = astar(graph, zero, node, goal, show=False)
        costs[node] = cost
    return costs


def audit(graph, h, goal, true):
    print("Admissibility check: h(n) <= true remaining cost.")
    for n in graph:
        print(n, "| h:", h[n], "| true cost:", true[n], "| ok:", h[n] <= true[n])
    print("Consistency check: h(u) <= cost(u,v) + h(v) for every edge.")
    for u in graph:
        for v, w in graph[u]:
            print(u, "->", v, "|", h[u], "<=", w, "+", h[v], "=", w + h[v],
                  "| ok:", h[u] <= w + h[v])


if __name__ == "__main__":
    print("A* with the supplied heuristic:")
    cost, path, expanded = astar(graph, h, "S", "G")
    print("A* path:", path)
    print("A* cost:", cost, "| checked again:", path_cost(path))
    print("A* expanded nodes:", expanded, "| count:", len(expanded))
    print()
    print("UCS control (all h = 0):")
    zero = {n: 0 for n in h}
    cost2, path2, expanded2 = astar(graph, zero, "S", "G")
    print("UCS path:", path2)
    print("UCS cost:", cost2, "| checked again:", path_cost(path2))
    print("UCS expanded nodes:", expanded2, "| count:", len(expanded2))
    print()
    print("Heuristic audit:")
    true = true_costs(graph, "G")
    audit(graph, h, "G", true)
    print()
    print("Overestimate test: only h(C) changes from 2 to 10.")
    h_bad = dict(h)
    h_bad["C"] = 10
    cost3, path3, expanded3 = astar(graph, h_bad, "S", "G")
    print("A* path with h(C) = 10:", path3)
    print("A* cost with h(C) = 10:", cost3, "| checked again:", path_cost(path3))
    print("Expanded nodes:", expanded3, "| count:", len(expanded3))
