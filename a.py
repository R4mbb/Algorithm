import time
start_time = time.time()

for _ in range(10000):
    for _ in range(10000):
        pass

end_time = time.time()

print(f"time : {end_time - start_time}")
