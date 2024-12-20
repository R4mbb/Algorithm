N, M, K = map(int, input().split())
data = list(map(int, input().split()))

result = 0

data.sort()
first = data[N-1]
second = data[N-2]

count = int(M / (K+1))
count += M % (K+1)

result += count * first
result += (M-count) * second

print(result)
