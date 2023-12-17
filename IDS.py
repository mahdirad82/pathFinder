from successor import get_successors
from input import standardMatrix


class Node:
    def __init__(self, state, cost, path):
        self.state = state
        self.cost = cost
        self.path = path


def ids(start, targets):
    depth = 0
    while True:
        result = dls(start, targets, depth)
        if result:
            return result
        depth += 1
        if len(standardMatrix) * len(standardMatrix[0]) < depth:
            return []


def dls(start, targets, depth, path=[]):
    if depth == 0 and targets <= set(path + [start]):
        return path + [start]
    if depth > 0:
        for successor in get_successors(start):
            if successor not in path:
                new_path = path + [start]
                result = dls(successor, targets, depth - 1, new_path)
                if result:
                    return result
    return None
