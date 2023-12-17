from queue import Queue
from successor import get_successors
from input import targets

targets = set(targets)


def heuristic(state):
    distances = [
        abs(state[0] - target[0]) + abs(state[1] - target[1]) for target in targets
    ]
    return min(distances)


def best_first_search(start, remainingTargets):
    queue = Queue()
    queue.put(start)
    stack = []
    visited = set()
    path = []

    while not queue.empty():
        current_state = queue.get()

        if current_state not in visited:
            visited.add(current_state)

        if current_state in remainingTargets:
            remainingTargets.discard(current_state)
            targets.discard(current_state)

        path.append(current_state)

        if remainingTargets == set():
            return path

        successors = []
        for state in get_successors(current_state):
            if state not in visited:
                successors.append(state)

        successors.sort(key=heuristic)
        while len(successors) == 0:
            path.pop()
            if len(stack) == 0:
                return []
            prev = stack.pop()
            successors = []
            for state in get_successors(prev):
                if state not in visited:
                    successors.append(state)

            successors.sort(key=heuristic)

        queue.put(successors[0])
        stack.append(current_state)
        successors.clear()

    return []
