from queue import Queue
from successor import get_successors, newMatrix, initial_state, targets


class BFS:
    def __init__(self, initial_state, targets):
        self.initial_state = initial_state
        self.targets = set(targets)
        self.queue = Queue()
        self.paths = []
        self.best_cost = 999999999
        self.best_path = []

    def search(self):
        self.queue.put(
            (
                self.initial_state,
                [self.initial_state],
                newMatrix[self.initial_state[0]][self.initial_state[1]],
            )
        )

        while not self.queue.empty():
            current_state, current_path, total_cost = self.queue.get()

            if self.targets <= set(current_path):
                if set(current_path) not in self.paths:
                    self.paths.append(set(current_path))

                    if total_cost < self.best_cost:
                        self.best_path = current_path
                        self.best_cost = total_cost
                else:
                    return

            for successor_state in get_successors(current_state):
                if successor_state not in current_path:  # Avoid cycles
                    new_path = list(current_path)
                    new_path.append(successor_state)

                    new_cost = (
                        total_cost + newMatrix[successor_state[0]][successor_state[1]]
                    )
                    self.queue.put((successor_state, new_path, new_cost))

        if len(self.best_path) == 0:
            print("there is no route")


bfs = BFS(initial_state, targets)
bfs.search()
