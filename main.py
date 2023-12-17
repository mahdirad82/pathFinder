import time
from bestFirstSearch import best_first_search
from input import initial_state, standardMatrix, targets
from BFS import BFS_Algorithm
from DFS import dfs
from IDS import ids
from UCS import UCS_Algorithm


def calculateEnergyAndPath(path):
    if len(path) == 0:
        return "there is no route!"
    energy = 500
    prev = None
    string = ""
    for state in path:
        if prev:
            if state[0] > prev[0]:
                string += "D"
            elif state[0] < prev[0]:
                string += "U"
            elif state[1] > prev[1]:
                string += "R"
            elif state[1] < prev[1]:
                string += "L"
        energy -= standardMatrix[state[0]][state[1]]
        prev = state
    return (energy, string)


bfs = BFS_Algorithm(initial_state, targets)
start = time.time()
print("BFS: ", end="")
print(calculateEnergyAndPath(bfs.search()), end=", ")
end = time.time()
print(int(end - start))

print("DFS: ", end="")
start = time.time()
print(calculateEnergyAndPath(dfs(initial_state, set(targets))), end=", ")
end = time.time()
print(int(end - start))

print("IDS: ", end="")
start = time.time()
print(calculateEnergyAndPath(ids(initial_state, set(targets))), end=", ")
end = time.time()
print(int(end - start))

ucs = UCS_Algorithm(initial_state, targets)
start = time.time()
print("UCS: ", end="")
print(calculateEnergyAndPath(ucs.search()), end=", ")
end = time.time()
print(int(end - start))


print("Greedy: ", end="")
start = time.time()
print(calculateEnergyAndPath(best_first_search(initial_state, set(targets))), end=", ")
end = time.time()
print(int(end - start))
