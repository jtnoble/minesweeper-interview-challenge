import pytest
from py_check.main import minesweeper, get_neighbors, count_neighbor_mines
from textwrap import dedent

"""

*...
....
.*..
....


*100
2210
1*10
1110

"""

def test_minesweeper() -> None:
    example = dedent('''
        *...
        ....
        .*..
        ....
    ''').strip()

    goal = dedent('''
        *100
        2210
        1*10
        1110
    ''').strip()

    result = minesweeper(example)

    assert result == goal

def test_get_neighbors():
    matrix = [
        ['.', '.', '.', '.'],
        ['.', '.', '*', '.'],
        ['.', '.', '.', '.'],
    ]
    result = get_neighbors(matrix, 1, 1)
    expected = '*.......'
    assert result == expected

def test_get_neighbors_top_left():
    matrix = [
        ['.', '.', '.', '.'],
        ['.', '*', '*', '.'],
        ['.', '.', '.', '.'],
    ]
    result = get_neighbors(matrix, 0, 0)
    expected = '..*'
    assert result == expected

def test_get_neighbors_top_right():
    matrix = [
        ['.', '.', '.', '.'],
        ['.', '*', '*', '.'],
        ['.', '.', '.', '.'],
    ]
    result = get_neighbors(matrix, 0, 3)
    expected = '..*'
    assert result == expected

def test_get_neighbors_bottom_left():
    matrix = [
        ['.', '.', '.', '.'],
        ['.', '*', '*', '.'],
        ['.', '.', '.', '.'],
    ]
    result = get_neighbors(matrix, 2, 0)
    expected = '..*'
    assert result == expected

def test_get_neighbors_bottom_right():
    matrix = [
        ['.', '.', '.', '.'],
        ['.', '*', '*', '.'],
        ['.', '.', '.', '.'],
    ]
    result = get_neighbors(matrix, 2, 3)
    expected = '..*'
    assert result == expected

@pytest.mark.parametrize("line, count", (
    ("..*...", 1),
    ("****.***", 7),
))
def test_count_neighbor_mines(line: str, count: int) -> None:
    """Check that amount of *s is counted correctly"""

    result = count_neighbor_mines(line)
    assert result == count


