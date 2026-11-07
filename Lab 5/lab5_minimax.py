import math


def minimax(curDepth, nodeIndex, maxTurn, scores, targetDepth):
    global minimax_leaves
    if curDepth == targetDepth:
        minimax_leaves = minimax_leaves + 1
        return scores[nodeIndex]
    if maxTurn:
        return max(
            minimax(curDepth + 1, nodeIndex * 2, False, scores, targetDepth),
            minimax(curDepth + 1, nodeIndex * 2 + 1, False, scores, targetDepth)
        )
    else:
        return min(
            minimax(curDepth + 1, nodeIndex * 2, True, scores, targetDepth),
            minimax(curDepth + 1, nodeIndex * 2 + 1, True, scores, targetDepth)
        )


def alphabeta(depth, index, maxTurn, scores, target, alpha, beta):
    global alphabeta_leaves
    if depth == target:
        alphabeta_leaves = alphabeta_leaves + 1
        return scores[index]
    if maxTurn:
        value = float("-inf")
        for i in range(2):
            value = max(value, alphabeta(depth + 1, index * 2 + i, False, scores, target, alpha, beta))
            alpha = max(alpha, value)
            if alpha >= beta:
                break
        return value
    else:
        value = float("inf")
        for i in range(2):
            value = min(value, alphabeta(depth + 1, index * 2 + i, True, scores, target, alpha, beta))
            beta = min(beta, value)
            if alpha >= beta:
                break
        return value


minimax_leaves = 0
alphabeta_leaves = 0

scores = [3, 5, 2, 9, 0, 7]
treeDepth = math.ceil(math.log2(len(scores)))
scores += [0] * (2 ** treeDepth - len(scores))
print("Minimax scores:", scores)
print("Minimax value:", minimax(0, 0, True, scores, treeDepth))
print("Minimax leaves evaluated:", minimax_leaves)
print()
print("Hand trace of the same tree:")
print("Leaves:", scores)
print("Depth 2 (MAX):", max(scores[0], scores[1]), max(scores[2], scores[3]), max(scores[4], scores[5]), max(scores[6], scores[7]))
print("Depth 1 (MIN):", min(max(scores[0], scores[1]), max(scores[2], scores[3])), min(max(scores[4], scores[5]), max(scores[6], scores[7])))
print("Root (MAX):", max(min(max(scores[0], scores[1]), max(scores[2], scores[3])), min(max(scores[4], scores[5]), max(scores[6], scores[7]))))
print()

scores2 = [3, 5, 2, 9, 3, 5, 2, 9]
depth2 = int(math.log2(len(scores2)))
minimax_leaves = 0
alphabeta_leaves = 0
print("Same tree for both:")
print("Scores:", scores2)
print("Minimax value:", minimax(0, 0, True, scores2, depth2))
print("Minimax leaves evaluated:", minimax_leaves)
print("Alpha-beta value:", alphabeta(0, 0, True, scores2, depth2, float("-inf"), float("inf")))
print("Alpha-beta leaves evaluated:", alphabeta_leaves)
print()

scores3 = [9, 2, 5, 3, 9, 2, 5, 3]
depth3 = int(math.log2(len(scores3)))
minimax_leaves = 0
alphabeta_leaves = 0
print("Reordered branches:")
print("Scores:", scores3)
print("Minimax value:", minimax(0, 0, True, scores3, depth3))
print("Minimax leaves evaluated:", minimax_leaves)
print("Alpha-beta value:", alphabeta(0, 0, True, scores3, depth3, float("-inf"), float("inf")))
print("Alpha-beta leaves evaluated:", alphabeta_leaves)
print()

scores4 = [7]
minimax_leaves = 0
alphabeta_leaves = 0
print("Edge case, one leaf:")
print("Scores:", scores4)
print("Minimax value:", minimax(0, 0, True, scores4, 0))
print("Minimax leaves evaluated:", minimax_leaves)
print("Alpha-beta value:", alphabeta(0, 0, True, scores4, 0, float("-inf"), float("inf")))
print("Alpha-beta leaves evaluated:", alphabeta_leaves)
print()

scores5 = [4, 4, 4, 4, 4, 4, 4, 4]
depth5 = int(math.log2(len(scores5)))
minimax_leaves = 0
alphabeta_leaves = 0
print("Edge case, all leaves equal:")
print("Scores:", scores5)
print("Minimax value:", minimax(0, 0, True, scores5, depth5))
print("Minimax leaves evaluated:", minimax_leaves)
print("Alpha-beta value:", alphabeta(0, 0, True, scores5, depth5, float("-inf"), float("inf")))
print("Alpha-beta leaves evaluated:", alphabeta_leaves)
