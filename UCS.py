from queue import Queue
from successor import get_successors, newMatrix, initial_state, targets


class UCS:
    def __init__(self, initial_state, targets):
        self.initial_state = initial_state
        self.targets = set(targets)
        self.queue = Queue()
        self.best_path = []

    def getCost(self, state):
        return newMatrix[state[0]][state[1]]

    def search(self):
        self.queue.put((self.initial_state, [self.initial_state]))

        while not self.queue.empty():
            current_state, current_path = self.queue.get()

            if self.targets <= set(current_path):
                self.best_path = current_path
                return

            successorOfCurrentState = get_successors(current_state)
            successorOfCurrentState.sort(key=self.getCost)

            for successor_state in successorOfCurrentState:
                if successor_state not in current_path:  # Avoid cycles
                    new_path = list(current_path)
                    new_path.append(successor_state)
                    self.queue.put((successor_state, new_path))

        if len(self.best_path) == 0:
            print("there is no route")


bfs = UCS(initial_state, targets)
bfs.search()
print(bfs.best_path)
