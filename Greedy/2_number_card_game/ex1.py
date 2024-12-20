row, column = map(int, input().split())

result = 0

for i in range(row):
    data = list(map(int, input().split()))
    m = min(data)

    if result < m:
        result = m

print(result)
