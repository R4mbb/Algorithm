rows, cols = map(int, input().split())
x, y, vec = map(int, input().split())

data = []
d = [[0] * cols for _ in range(rows)]

d[x][y] = 1

for i in range(rows):
    data.append(list(map(int, input().split())))

dx = [-1, 0, 1, 0]
dy = [0, 1, 0, -1]

def turn_left():
    global vec
    vec -= 1
    if vec == -1:
        vec = 3

count = 1
turn_time = 0

while True:
    turn_left()
    nx = x + dx[vec]
    ny = y + dy[vec]

    if d[nx][ny] == 0 and data[nx][ny] == 0:
        d[nx][ny] = 1
        x = nx
        y = ny
        count += 1
        turn_time = 0
        continue
    else:
        turn_time += 1

    if turn_time == 4:
        nx = x - dx[vec]
        ny = y - dy[vec]

        if data[nx][ny] == 0:
            x = nx
            y = ny
        else:
            break

        turn_time = 0

print(count)
