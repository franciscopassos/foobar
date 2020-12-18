from collections import deque, namedtuple


BOARD = [range(64)[x:x+8]
         for x in range(0, 64, 8)]


POSITIONS = {value: (i, j)
             for i, row in enumerate(BOARD)
             for j, value in enumerate(row)}


Node = namedtuple('Node', ['i', 'j', 'depth'])


def generate_neighbours(node):
    for di, dj in [(-1, -2),
                   (-2, -1),
                   (-1, +2),
                   (-2, +1),
                   (+1, +2),
                   (+2, +1),
                   (+1, -2),
                   (+2, -1)]:
        vi, vj = node.i + di, node.j + dj
        if 0 <= vi < len(BOARD) and 0 <= vj < len(BOARD[0]):
            yield Node(vi, vj, node.depth + 1)


def solution(src, dest):             # BFS-based
    visited = {}                     # Nodes indexed by (i, j)
    frontier = deque()
    i, j = POSITIONS[src]
    frontier.append(Node(i, j, 0))
    while frontier:
        node = frontier.popleft()
        if (node.i, node.j) == POSITIONS[dest]:
            return node.depth
        frontier.extend([nb for nb in generate_neighbours(node)
                         if (nb.i, nb.j) not in visited])
        visited[(node.i, node.j)] = node