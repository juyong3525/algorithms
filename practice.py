import time

start_time = time.time()

total = 0

for i in range(1, 10000001):
    total += i

end_time = time.time()

print(total)
print(end_time - start_time)
