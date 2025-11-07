from dataclasses import dataclass

# "....\n..*."

# ['.', '.' ...], ['.', '.']

def minesweeper(sweep_text: str) -> str:
    result = ""
    separate_lines = sweep_text.splitlines()
    # current ['*...', '....', '.*..', '....']

    matrix = []
    for line in separate_lines:
        matrix.append(list(line))
    
    # new ['*...']
    #     ['....']

    for row in range(len(matrix)):
        for col in range(len(matrix[row])):
            if matrix[row][col] == "*":
                result += "*"
                continue
            neighbors = get_neighbors(matrix, row, col)
            neighbor_count = count_neighbor_mines(neighbors)
            result += str(neighbor_count)
        result += '\n'
    return result.strip()


def get_neighbors(matrix: list[list], row: int, col: int) -> str:
    values = ""
    
    # right
    if col + 1 < len(matrix[row]):
        values += matrix[row][col+1]
    
    # left
    if col - 1 >= 0:
        values += matrix[row][col-1]

    # up
    if row + 1 < len(matrix):
        values += matrix[row+1][col]

    # down right
    if col + 1 < len(matrix[row]) and row + 1 < len(matrix):
        values += matrix[row+1][col+1]

    # down left
    if col - 1 >= 0 and row + 1 < len(matrix):
        values += matrix[row+1][col-1]

    # up
    if row - 1 >= 0:
        values += matrix[row-1][col]
    
    # up right
    if row - 1 >= 0 and col + 1 < len(matrix[row]):
        values += matrix[row-1][col+1]

    # up left
    if row - 1 >= 0 and col - 1 >= 0:
        values += matrix[row-1][col-1]

    return values


def count_neighbor_mines(line: str) -> int:
    return line.count('*')

if __name__ == "__main__":
    print("\n\nHello World!\n\n")

    minesweeper()
