from successor import get_successors


def dfs(start, targets):
    stack = [(start, [start])]
    while stack:
        state, path = stack.pop()

        if targets <= set(path):
            return path

        for successor in get_successors(state):
            if successor not in set(path):
                stack.append((successor, path + [successor]))

    return []
