class Solution:
    def hasPath(self, maze: List[List[int]], start: List[int], destination: List[int]) -> bool:
        def dfs(x, y):
            # return if the ball can stop at destination if starting at (x, y)
            if [x, y] == destination:
                return True
            if (x, y) in visited:
                return False
            visited.add((x, y))
            for dx, dy in [(-1, 0), (1, 0), (0, -1), (0, 1)]:
                new_x, new_y = x, y
                # the ball rolls until hitting a wall
                while 0 <= new_x + dx < row and 0 <= new_y + dy < col and maze[new_x + dx][new_y + dy] == 0:
                    new_x += dx
                    new_y += dy
                if dfs(new_x, new_y):
                    return True
            return False

        row, col = len(maze), len(maze[0])
        visited = set()
        return dfs(start[0], start[1])
