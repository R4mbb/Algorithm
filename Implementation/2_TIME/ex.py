import sys, time

n = int(sys.stdin.readline())

result = 0

start = time.time()
for i in range(n+1):
    if "3" in str(i):
        result += 60*60
        continue
    for j in range(60):
        if "3" in str(j):
            result += 60
            continue
        for k in range(60):
            if "3" in str(k):
                result += 1


print(result)
print(time.time()-start)
