# You are given an m x n matrix maze (0-indexed) with empty cells (represented as '.') and walls (represented as '+'). You are also given the entrance of the maze, where entrance = [entrancerow, entrancecol] denotes the row and column of the cell you are initially standing at.

# In one step, you can move one cell up, down, left, or right. You cannot step into a cell with a wall, and you cannot step outside the maze. Your goal is to find the nearest exit from the entrance. An exit is defined as an empty cell that is at the border of the maze. The entrance does not count as an exit.

# Return the number of steps in the shortest path from the entrance to the nearest exit, or -1 if no such path exists.

class Maze:
    def __init__(self, maze: List[List[str]], entrance: List[int]):
        self.maze: List[List[str]] = maze
        self.entrance: List[int] = entrance
        self.rows: int = len(maze)
        self.cols: int = len(maze[0])
        self.visited: List[List[bool]] = [[False for _ in range(self.cols)] for _ in range(self.rows)]
        self.directions: List[tuple(int)] = [(1, 0), (-1, 0), (0, 1), (0, -1)]

    def is_valid(self, x: int, y: int) -> bool:
        return 0 <= x < self.rows and 0 <= y < self.cols and self.maze[x][y] == "."

    def is_exit(self, x: int, y: int) -> bool:
        return (x == 0 or x == self.rows - 1 or y == 0 or y == self.cols - 1) and [x, y] != self.entrance

    def find_shortest_exit(self):
        queue = deque([(self.entrance[0], self.entrance[1], 0)])  # (x, y, steps)
        self.visited[self.entrance[0]][self.entrance[1]] = True

        while queue:
            x, y, steps = queue.popleft()

            if self.is_exit(x, y):
                return steps

            for dx, dy in self.directions:
                new_x, new_y = x + dx, y + dy
                if self.is_valid(new_x, new_y) and not self.visited[new_x][new_y]:
                    self.visited[new_x][new_y] = True
                    queue.append((new_x, new_y, steps + 1))

        return -1


class Solution:
    def nearestExit(self, maze: List[List[str]], entrance: List[int]) -> int:
        x = Maze(maze, entrance)
        return x.find_shortest_exit()
