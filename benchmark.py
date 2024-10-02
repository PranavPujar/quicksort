import time
import random
import matplotlib.pyplot as plt
from quicksort import quicksort

def generate_best_case(n):
    return list(range(n))

def generate_worst_case(n):
    return list(range(n, 0, -1))

def generate_average_case(n):
    return [random.randint(1, 1000) for _ in range(n)]

def benchmark(sort_func, input_generator, sizes):
    times = []
    for n in sizes:
        arr = input_generator(n)
        start_time = time.time()
        sort_func(arr)
        end_time = time.time()
        times.append(end_time - start_time)
    return times

sizes = [100, 500, 1000, 5000, 10000, 50000]

best_case_times = benchmark(quicksort, generate_best_case, sizes)
worst_case_times = benchmark(quicksort, generate_worst_case, sizes)
average_case_times = benchmark(quicksort, generate_average_case, sizes)

plt.figure(figsize=(10, 6))
plt.plot(sizes, best_case_times, 'g-', label='Best Case')
plt.plot(sizes, worst_case_times, 'r-', label='Worst Case')
plt.plot(sizes, average_case_times, 'b-', label='Average Case')
plt.xlabel('Input Size (n)')
plt.ylabel('Time (seconds)')
plt.title('Quicksort Performance')
plt.legend()
plt.xscale('log')
plt.yscale('log')
plt.grid(True)
plt.savefig('quicksort_benchmark.png')
plt.show()

print("Best case times:", best_case_times)
print("Worst case times:", worst_case_times)
print("Average case times:", average_case_times)