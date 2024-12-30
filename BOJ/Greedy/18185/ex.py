# 시간초과
import sys, time
#n = int(input())
n = int(sys.stdin.readline())
data = list(map(int, sys.stdin.readline().split()))

result = 0

a = time.time()
while True:
    for num in range(n):
        #print(f"data : {data}\nnum : {num}")
        if data[num] > 0:
            if (num+2) <= len(data)-1:
                if data[num+1] and data[num+2] > 0 and data[num+1] <= data[num+2] and data[num] <= data[num+1]:
                    result += 7
                    data[num] -= 1
                    data[num+1] -= 1
                    data[num+2] -= 1
                    break
                elif data[num+1] > 0 and data[num] <= data[num+1]:
                    result += 5
                    data[num] -= 1
                    data[num+1] -= 1
                    break
                else:
                    result += 3
                    data[num] -= 1
                    break
            elif (num+1) <= len(data)-1:
                if data[num+1] > 0 and data[num] <= data[num+1]:
                    result += 5
                    data[num] -= 1
                    data[num+1] -= 1
                    break
                else:
                    result += 3
                    data[num] -= 1
                    break
            result += 3
            data[num] -= 1
            break
    c = sum(data)
    if c == 0:
        break

print(result)
a = time.time() - a
print(a)
