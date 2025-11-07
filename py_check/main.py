def minesweeper(sweep_text: str) -> str:
    """
    Input: string input of minesweeper board
        example: '*...\n....\n.*..\n....'
    Output: string output of board with number of mines next to a space. 
        example: '*100\n2210\n1*10\n1110'
    """
    result = ""
    separate_lines = sweep_text.splitlines() # ['*...', '....', '.*..', '....']

    matrix = [line for line in separate_lines]
    # matrix = ['*...']
    #          ['....']
    #          ['.*..']
    #          ['....']

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
    """Given a matrix, row, and column, return a string of only row,col coords and its surrounding neighbors"""
    values = []
    
    # right
    if col + 1 < len(matrix[row]):
        values.append(matrix[row][col+1])
    
    # left
    if col - 1 >= 0:
        values.append(matrix[row][col-1])

    # up
    if row + 1 < len(matrix):
        values.append(matrix[row+1][col])

    # down right
    if col + 1 < len(matrix[row]) and row + 1 < len(matrix):
        values.append(matrix[row+1][col+1])

    # down left
    if col - 1 >= 0 and row + 1 < len(matrix):
        values.append(matrix[row+1][col-1])

    # up
    if row - 1 >= 0:
        values.append(matrix[row-1][col])
    
    # up right
    if row - 1 >= 0 and col + 1 < len(matrix[row]):
        values.append(matrix[row-1][col+1])

    # up left
    if row - 1 >= 0 and col - 1 >= 0:
        values.append(matrix[row-1][col-1])

    return "".join(values)


def count_neighbor_mines(line: str) -> int:
    """Count the amount of mines in a string"""
    return line.count('*')

if __name__ == "__main__":
    test_input = '*...\n....\n.*..\n....'
    output = minesweeper(test_input)
    print(f'Input:\n{test_input}\n\nOutput:\n{output}')

