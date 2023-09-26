
import random , time

start = time.perf_counter()

np_element = 1000000000

print(random.shuffle(list(range(np_element)),int(np_element/2)))
end = time.perf_counter() - start

print(end)