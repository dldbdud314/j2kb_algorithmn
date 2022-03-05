def dfs(grid, curI, curJ):
    #탐색하지 않고 return
    #좌표가 범위를 벗어났거나, 이미 방문한 경우
    if curI < 0 or curI >= len(grid) or curJ < 0 or curJ >= len(grid[0]) or grid[curI][curJ] == "0":
        return
    
    grid[curI][curJ] = "0" #방문 표시(1->0)
    
    dirs = [[-1, 0], [0, 1], [1, 0], [0, -1]] #위, 오, 아래, 왼
    for dir in dirs:
        nextI = curI + dir[0]
        nextJ = curJ + dir[1]
        dfs(grid, nextI, nextJ)

def numIslands(grid):
    cnt = 0
    for i in range(len(grid)):
        for j in range(len(grid[0])):
            if grid[i][j] == "1": #방문하지 않은 곳이면 탐색
                dfs(grid, i, j) 
                cnt += 1 #한 island 탐색 완료 했으므로 면적 +1
    return cnt