from main import matrix


def numerisingMatrix(matrix):
    targets = []
    initial_state = None
    for i in range(len(matrix)):
        for j in range(len(matrix[i])):
            if "R" in matrix[i][j]:
                matrix[i][j] = matrix[i][j].replace("R", "")
                initial_state = (i, j)
            elif "T" in matrix[i][j]:
                matrix[i][j] = matrix[i][j].replace("T", "")
                targets.append((i, j))
            if matrix[i][j].isdigit():
                matrix[i][j] = int(matrix[i][j])

            elif "C" in matrix[i][j]:
                matrix[i][j] = matrix[i][j].replace("C", "")
                matrix[i][j] = int(matrix[i][j]) - 10
            elif "B" in matrix[i][j]:
                matrix[i][j] = matrix[i][j].replace("B", "")
                matrix[i][j] = int(matrix[i][j]) - 5
            elif "I" in matrix[i][j]:
                matrix[i][j] = matrix[i][j].replace("I", "")
                matrix[i][j] = int(matrix[i][j]) - 12

    return [matrix, initial_state, targets]


standardMatrix, initial_state, targets = numerisingMatrix(matrix)


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

    if x < 0 or x >= len(matrix) or y < 0 or y >= len(matrix[0]):
        return False

    if matrix[x][y] == "X":
        return False
    return True
