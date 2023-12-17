from input import standardMatrix


def get_successors(curr_pos):
    successors = []

    movements = [(0, -1), (1, 0), (0, 1), (-1, 0)]

    for move in movements:
        new_pos = (curr_pos[0] + move[0], curr_pos[1] + move[1])
        if is_valid_move(new_pos):
            successors.append(new_pos)

    return successors


# Define the function to check if a move is valid
def is_valid_move(pos):
    x, y = pos

    if x < 0 or x >= len(standardMatrix) or y < 0 or y >= len(standardMatrix[0]):
        return False

    if standardMatrix[x][y] == "X":
        return False
    return True
