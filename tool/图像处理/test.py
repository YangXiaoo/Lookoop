row = 5
col = 6
img =  [[0, 0, 0, 1, 1, 0],
        [0, 1, 1, 2, 3,0],
        [5, 1, 0, 0, 4, 2],
        [0, 8, 7, 8, 5, 0],
        [0, 0, 0, 0, 0, 0]]
visited = [[False for _ in range(col)] for _ in range(row)] 
print(visited)
queue = [] # 存放每一次遍历的起点
def bfs(img, row, col, visited):
    m, n = row, col
    queue.append([row, col])
    visited[row][col] = True 

    while len(queue) != 0:
        print(queue)
        row, col = queue.pop()
        # print(len(queue))
        
        # 往左搜索
        if row > 1 and not visited[row - 1][col] and img[row - 1][col] == 0:
            queue.append([row - 1, col])
            visited[row - 1][col] = True

        # 往右搜索
        if row + 1 < m and not visited[row + 1][col] and img[row + 1][col] == 0:
            queue.append([row + 1, col])
            visited[row + 1][col] = True

        # 往上搜索
        if col - 1 >= 0 and not visited[row][col - 1] and img[row][col - 1] == 0:
            queue.append([row, col -1])
            visited[row][col - 1] = True

        # 往下搜搜
        if col + 1 < n and not visited[row][col + 1] and img[row][col + 1] == 0:
            queue.append([row, col + 1])
            visited[row][col + 1] = True

# 第一行与最后一行开始
for c in range(col):
    if not visited[0][c] and img[0][c] == 0:
        bfs(img, 0, c, visited)
    if not visited[-1][c] and img[-1][c] == 0:
        bfs(img, row - 1, c, visited)


for r in range(row):
    if not visited[r][0] and img[r][0] == 0:
        bfs(img, r, 0, visited)
    if not visited[r][-1] and img[r][-1] == 0:
        bfs(img, r, col - 1, visited)

# 将模板二值化0,1
for i in range(row):
    for j in range(col):
        if not visited[i][j]:
            img[i][j] = 1
print(img)
print(visited)
# 原img
# [[0, 0, 0, 1, 1, 0],
#  [0, 1, 1, 2, 3,0],
#  [5, 1, 0, 0, 4, 2],
#  [0, 8, 7, 8, 5, 0],
#  [0, 0, 0, 0, 0, 0]]

# 处理过后的img
# [[0, 0, 0, 1, 1, 0], 
#  [0, 1, 1, 1, 1, 0], 
#  [1, 1, 1, 1, 1, 1], 
#  [0, 1, 1, 1, 1, 0], 
#  [0, 0, 0, 0, 0, 0]]


# # 原visited
# [[False, False, False, False, False, False], 
#  [False, False, False, False, False, False], 
#  [False, False, False, False, False, False], 
#  [False, False, False, False, False, False], 
#  [False, False, False, False, False, False]]

# # visited
# [[True, True, True, False, False, True], 
#  [True, False, False, False, False, True], 
#  [False, False, False, False, False, False], 
#  [True, False, False, False, False, True], 
#  [True, True, True, True, True, True]]






