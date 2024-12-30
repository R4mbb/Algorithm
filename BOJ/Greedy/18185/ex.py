# 시간초과
n = int(input())
data = list(map(int, input().split()))

result = 0
c = sum(data)

while c > 0:
    for num in range(n):
        if data[num] > 0:
            if (num+1) <= len(data)-1:
                if data[num+1] > 0 and data[num] <= data[num+1]:
                    if (num+2) <= len(data)-1:
                        if data[num+2] > 0 and data[num+1] <= data[num+2]:
                            result += 7

                            for j in range(num, num+3):
                                data[j] -= 1
                            break
                
                    result += 5

                    for j in range(num, num+2):
                        data[j] -= 1
                    break

                result += 3
                data[num] -= 1
                break

            result += 3
            data[num] -= 1
            break
    c = sum(data)

print(result)
