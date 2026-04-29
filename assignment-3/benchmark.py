from sortingAlgos import insertion_sort, merge_sort, quick_sort
import time
import random

def run_performance_test():
    sizes = [1000, 5000, 10000]
    data_types = ["Random", "Sorted", "Reverse"]

    for n in sizes:
        print(f"\n--- Array Size: {n} ---")
        for d_type in data_types:
            if d_type == "Random": data = random.sample(range(n * 10), n)
            elif d_type == "Sorted": data = list(range(n))
            else: data = list(range(n, 0, -1))

            # Performance measurement for each sorting algorithm
            start = time.time()
            insertion_sort(data.copy())
            print(f"InsertionSort ({d_type}): {time.time() - start:.4f}s")

            start = time.time()
            merge_sort(data.copy())
            print(f"MergeSort ({d_type}): {time.time() - start:.4f}s")

            start = time.time()
            quick_sort(data.copy())
            print(f"QuickSort ({d_type}): {time.time() - start:.4f}s")

if __name__ == "__main__":
    run_performance_test()