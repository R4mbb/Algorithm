row, column = map(int, input().split())

result = 0

for i in range(row):
    data = list(map(int, input().split()))
    
    m = 10001

    for j in data:
        if j < m:
            m = j

    if result < m:
        result = m

print(result)

