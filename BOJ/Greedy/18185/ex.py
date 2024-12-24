# 안풀림 ㅋㅋㅋ

n = int(input())
data = list(map(int, input().split()))

data.sort(reverse=True)
c = 0
result = 0

for i in data:
    if i == 0:
        c = 0
    elif i >= 1:
        if c == 0:
            result += 3*i
            c = 1
        else:
            result += 2*i

print(result)
        
