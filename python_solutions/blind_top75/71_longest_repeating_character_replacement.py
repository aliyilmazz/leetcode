from collections import deque


class Solution:
    def pacificAtlantic_dfs(self, heights: List[List[int]]) -> List[List[int]]:

        m = len(heights)
        n = len(heights[0])

        directions = [(0, 1), (0, -1), (1, 0), (-1, 0)]

        dp_pacific = [[-1] * n for _ in range(m)]
        dp_atlantic = [[-1] * n for _ in range(m)]

        for i in range(m):
            dp_pacific[i][0] = True
            dp_atlantic[i][n - 1] = True

        for j in range(n):
            dp_pacific[0][j] = True
            dp_atlantic[m - 1][j] = True

        # dp[i][j][0] = pacific for i,j
        # dp[i][j][1] = atlantic for i,j
        # -1 -> undiscovered
        # 0 -> false
        # 1 -> True

        directions = [(-1, 0), (0, -1), (1, 0), (0, 1)]

        def dfs_pacific(i, j, visited):
            if (i, j) in visited:
                return False

            visited.add((i, j))
            if dp_pacific[i][j] == True:
                return True

            for dir in directions:
                new_i, new_j = i + dir[0], j + dir[1]
                if 0 <= new_i < m and 0 <= new_j < n and \
                        heights[i][j] >= heights[new_i][new_j] and dfs_pacific(new_i, new_j, visited) == True:
                    dp_pacific[i][j] = True
                    return True

            dp_pacific[i][j] = False
            return False

        def dfs_atlantic(i, j, visited):
            if (i, j) in visited:
                return False

            visited.add((i, j))

            if dp_atlantic[i][j] == True:
                return True

            for dir in directions:
                new_i, new_j = i + dir[0], j + dir[1]
                if 0 <= new_i < m and 0 <= new_j < n and heights[i][j] >= heights[new_i][new_j]:
                    lowerheight = dfs_atlantic(new_i, new_j, visited)
                    if lowerheight:
                        dp_atlantic[i][j] = True
                        return True

            dp_atlantic[i][j] = False
            return False

        for i in range(1, m):
            for j in range(1, n):
                dfs_pacific(i, j, set())

        for i in range(m - 1, -1, -1):
            for j in range(n - 1, -1, -1):
                dfs_atlantic(i, j, set())

        coords = []
        for i in range(m):
            for j in range(n):
                if dp_pacific[i][j] == True and dp_atlantic[i][j] == True:
                    coords.append([i, j])
        return coords

    def pacificAtlantic(self, matrix):
        if not matrix or not matrix[0]:
            return []

        m, n = len(matrix), len(matrix[0])
        atlantic_queue, pacific_queue = deque(), deque()

        for i in range(m):
            pacific_queue.append((i, 0))
            atlantic_queue.append((i, n - 1))

        for i in range(n):
            pacific_queue.append((0, i))
            atlantic_queue.append((m - 1, i))

        directions = [(0, 1), (0, -1), (1, 0), (-1, 0)]

        def bfs(queue):
            visited = set()
            while queue:
                i, j = queue.popleft()

                visited.add((i, j))

                for direction in directions:
                    new_i, new_j = i + direction[0], j + direction[1]
                    if not (0 <= new_i < m and 0 <= new_j < n):
                        continue

                    if (new_i, new_j) in visited:
                        continue

                    if matrix[i][j] <= matrix[new_i][new_j]:
                        queue.append((new_i, new_j))
            return visited

        pacific_visited = bfs(pacific_queue)
        atlantic_visited = bfs(atlantic_queue)
        return list(pacific_visited.intersection(atlantic_visited))
