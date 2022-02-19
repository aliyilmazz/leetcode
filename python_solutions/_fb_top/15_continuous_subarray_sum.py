from enum import Enum

class GridElement(Enum):
    SPACE, HOUSE, OBSTACLE = 0, 1, 2


class Solution:
    def shortestDistance(self, grid: List[List[int]]) -> int:

        min_distance = float('inf')
        m, n = len(grid), len(grid[0])
        total_houses = 0
        directions = [(1,0), (-1,0), (0,1), (0,-1)]
        
        
        
        # for each space in grid, denoted by [i][j]:
        # distances[i][j][0] -> total distance to every house 
        # distances[i][j][1] -> total number of houses reached
        
        total = [[0 for _ in range(n)] for _ in range(m)]
        
        
        def bfs(i, j):
            
            queue = deque([(i, j)])
            visited = set((i,j))
            distance = 0
            while queue:
                for _ in range(len(queue)):
                    x, y = queue.popleft()

                    if grid[x][y] <= 0:
                        grid[x][y] -= 1
                        total[x][y] += distance
                        
                    
                    for dir in directions:
                        new_x, new_y = x+dir[0], y+dir[1]
                        if (new_x, new_y) in visited:
                            continue

                        if not (0<=new_x<m and 0<=new_y<n):
                            continue
                        
                        if grid[new_x][new_y] <= 0:
                            visited.add((new_x, new_y))
                            queue.append((new_x, new_y))
                        
                distance += 1
        
        
        # [1] count houses and start bfs from each house
        for i in range(m):
            for j in range(n):
                if grid[i][j] == GridElement.HOUSE.value:
                    total_houses += 1
                    bfs(i, j)
        
        
        # check all empty lands with houses count equal to totalhouses, find min ans
        
        for i in range(m):
            for j in range(n):
                if grid[i][j] != -total_houses:
                    continue
                    
                min_distance = min(min_distance, total[i][j])
                
                
                
                
        return min_distance if min_distance != float('inf') else -1
        
        
        