numOfRow = int(input("Enter number of row: "))


matrix = []

for i in range(numOfRow):
    matrix.append(input().split())


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
