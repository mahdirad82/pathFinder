from queue import Queue
from successor import get_successors


class BFS_Algorithm:
    def __init__(self, initial_state, targets):
        self.initial_state = initial_state
        self.targets = set(targets)
        self.queue = Queue()

    def search(self):
        self.queue.put(
            (
                self.initial_state,
                [self.initial_state],
            )
        )

        while not self.queue.empty():
            current_state, current_path = self.queue.get()

            if self.targets <= set(current_path):
                return current_path

            for successor_state in get_successors(current_state):
                if successor_state not in current_path:
                    self.queue.put((successor_state, current_path + [successor_state]))
        return []
