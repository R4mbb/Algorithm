import sys

n = int(sys.stdin.readline())
data = list(map(str, sys.stdin.readline().split()))

x, y = 1, 1
dx = [0, 0, -1, 1]
dy = [-1, 1, 0, 0]
move_type = ['L', 'R', 'U', 'D']

nx, ny = 0, 0

for i in data:
    for j in range(len(move_type)):
        if i == move_type[j]:
            nx = x + dx[j]
            ny = y + dy[j]
    if nx < 1 or ny < 1 or nx > n or ny > n:
        continue

    x, y = nx, ny

print(x,y)
