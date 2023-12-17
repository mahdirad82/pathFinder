from queue import Queue
from successor import get_successors
from input import standardMatrix


class UCS_Algorithm:
    def __init__(self, initial_state, targets):
        self.initial_state = initial_state
        self.targets = set(targets)
        self.queue = Queue()

    def getCost(self, state):
        return standardMatrix[state[0]][state[1]]

    def search(self):
        self.queue.put((self.initial_state, [self.initial_state]))

        while not self.queue.empty():
            current_state, current_path = self.queue.get()

            if self.targets <= set(current_path):
                return current_path

            successors = get_successors(current_state)
            successors.sort(key=self.getCost)

            for successor_state in successors:
                if successor_state not in current_path:
                    self.queue.put((successor_state, current_path + [successor_state]))

        return []
