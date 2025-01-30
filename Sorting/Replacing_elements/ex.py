n, k = map(int, input().split())

data = []
for _ in range(2):
    data.append(list(map(int, input().split())))

for _ in range(k):
    mx = min(data[0])
    mi = data[0].index(mx)
    mn = max(data[1])
    ni = data[1].index(mn)

    data[0][mi], data[1][ni] = data[1][ni], data[0][mi]

print(sum(data[0]))
