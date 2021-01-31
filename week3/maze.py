import math


def fastest_escape_length(maze, i=0, j=0):
    n = len(maze)
    m = len(maze[0])
    if i == n - 1 and j == m - 1:
        return 1
    maze[i][j] = 1
    paths = []
    for a, b in [(i - 1, j), (i, j - 1), (i + 1, j), (i, j + 1)]:
        if 0 <= a < n and 0 <= b < m and maze[a][b] == 0:
            paths.append(1 + fastest_escape_length(maze, a, b))
    maze[i][j] = 0
    return min(paths) if paths else math.inf


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
            for path in paths:
                result.append([(i, j), *path])
    maze[i][j] = 0
    onlyShortest = [path for path in result if len(path) == min(map(len, result))]
    return onlyShortest


def weighted_escape_length(maze, w, i=0, j=0):
    n = len(maze)
    m = len(maze[0])
    if i == n - 1 and j == m - 1:
        return 1
    value = maze[i][j]
    maze[i][j] = "V"
    paths = []
    for a, b in [(i - 1, j), (i, j - 1), (i + 1, j), (i, j + 1)]:
        if 0 <= a < n and 0 <= b < m and maze[a][b] != "V":
            if value == 1:
                paths.append(w + weighted_escape_length(maze, w, a, b))
            else:
                paths.append(1 + weighted_escape_length(maze, w, a, b))
    maze[i][j] = value
    return min(paths) if paths else math.inf


def weighted_escapes(maze, w, i=0, j=0):
    n = len(maze)
    m = len(maze[0])
    if i == n - 1 and j == m - 1:
        return [[(i, j)]]
    value = maze[i][j]
    maze[i][j] = "V"
    result = []
    for a, b in [(i - 1, j), (i, j - 1), (i + 1, j), (i, j + 1)]:
        if 0 <= a < n and 0 <= b < m and maze[a][b] != "V":
            paths = weighted_escapes(maze, w, a, b)
            for path in paths:
                result.append([(i, j), *path])
    maze[i][j] = value
    path_weights = []
    for path in result:
        path_weight = 0
        for i, j in path:
            if maze[i][j] == 1:
                path_weight += w
            else:
                path_weight += 1
        path_weights.append(path_weight)
    min_path_weight = min(path_weights) if path_weights else 0
    indexes_min_path = [
        i for i, value in enumerate(path_weights) if value == min_path_weight
    ]
    onlyShortest = [result[i] for i in indexes_min_path]
    return onlyShortest