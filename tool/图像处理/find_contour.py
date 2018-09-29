# 2018-9-28
# 提取轮廓
import cv2
import numpy as np

kernel = 3
img = cv2.imread("C:\\Study\\test\\out_pic\\thresh.jpg", 0) # 通过阈值处理后得二值图像
row, col = img.shape
visited = [[False for _ in range(col)] for _ in range(row)]

def isValidPoint(img, r, c):
    h, w = img.shape
    if r + kernel < h and r - kernel > 0 and c + kernel < w and c - kernel > 0:
        return True
    return False


def isMargin(img, r, c):
    # 检测点[r,c]是否为图像边缘
    h, w = img.shape
    gap = kernel // 2
    black = 0
    white = 0 
    ce = 0
    for i in range(r - gap, r + gap, 1):
        for j in range(c - gap, c + gap, 1):
            # print(i, j)
            if img[i][j] != 0:
                # print(img[i][j])
                black += 1
            else:
                white += 1
            if visited[i][j]:
                ce += 1
    if black > 0 and white > 0 and ce < 6:
        return True
    return False


print(row, col)
s_r = row // 2 # 起始点高度坐标
x = col // 2
if img[s_r][x] == 0:
    isout = True
else:
    isout = False


while x >= 0:
# 若从手掌外开始则遇到第一个非0值即为手掌边缘轮廓
    if isout:
        if img[s_r][x] != 0:
            s_c = x
            break
        else:
            pass
    else:
# 否则起始点为手掌内，当遍历到手掌边缘轮廓时img[s_r][x] == 0
        if img[s_r][x] == 0:
            s_c = x + 1 # 起始点坐标
            break
    x -= 1




mask = np.zeros((img.shape[0], img.shape[1]), np.uint8)

# print([s_r, s_c])
queue = []
visited[s_r][s_c] = True
queue.append([s_r, s_c])
while len(queue) != 0:
    r, c = queue.pop()
    if isValidPoint(img, r - 1, c) and not visited[r - 1][c]:
        if isMargin(img, r - 1, c):
            queue.append([r - 1, c])
            visited[r - 1][c] = True
    if isValidPoint(img, r + 1, c) and not visited[r + 1][c]:
        if isMargin(img, r + 1, c):
            queue.append([r + 1, c])
            visited[r + 1][c] = True

    if isValidPoint(img, r, c - 1) and not visited[r][c - 1]:
        if isMargin(img, r, c - 1):
            queue.append([r, c - 1])
            visited[r][c - 1] = True
    if isValidPoint(img, r, c + 1) and not visited[r][c + 1]:
        if isMargin(img, r, c + 1):
            queue.append([r, c + 1])
            visited[r][c + 1] = True

for i in range(row):
    for j in range(col):
        if visited[i][j]:
            mask[i][j] = 255

cv2.imwrite("C:\\Study\\test\\out_pic\\zontour.jpg", mask)

