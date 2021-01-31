import math


def fastest_escape_length(maze, i=0, j=0):
    n = len(maze)
    m = len(maze[0])
    if i == n - 1 and j == m - 1:
        return 1
    maze[i][j] = 1
    result = 0
    for a, b in [(i - 1, j), (i, j - 1), (i + 1, j), (i, j + 1)]:
        if 0 <= a < n and 0 <= b < m and maze[a][b] == 0:
            result += 1 + fastest_escape_length(maze, a, b)
    maze[i][j] = 0
    return result if result else math.inf


def fastest_escapes(maze, i=0, j=0):
    n = len(maze)
    m = len(maze[0])
    if i == n - 1 and j == m - 1:
        return [[(i, j)]]
    maze[i][j] = 1
    result = []
    for a, b in [(i - 1, j), (i, j - 1), (i + 1, j), (i, j + 1)]:
        if 0 <= a < n and 0 <= b < m and maze[a][b] == 0:
            paths = fastest_escapes(maze, a, b)
            print(paths)
            for path in paths:
                result.append([(i, j), *path])
    maze[i][j] = 0
    only_shortest = [path for path in result if len(path) == min(map(len, result))]
    return only_shortest


def weighted_escape_length(maze, w, i=0, j=0):
    pass


def weighted_escapes(maze, w, i=0, j=0):
    pass