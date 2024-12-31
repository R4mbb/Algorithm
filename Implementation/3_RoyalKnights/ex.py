pos = input()
row = int(pos[1])
col = int(ord(pos[0])) - int(ord('a')) + 1

step = [(-2, 1), (-2, -1), (2, 1), (2, -1), (1, 2), (1, -2), (-1, 2), (-1, -2)]

n_row = 0
n_col = 0
result = 0

print(f"row : {row}, col : {col}")
for i in step:
    n_row = row + i[0]
    n_col = col + i[1]
    print(f"n_row : {n_row}, n_col : {n_col}")

    if n_row <= 8 and n_row > 0 and n_col <= 8 and n_col > 0:
        result += 1

print(result)

