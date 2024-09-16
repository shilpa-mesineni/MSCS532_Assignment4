import time
import random

# Heapsort Implementation
def heapify(arr, n, i):
    largest = i
    left = 2 * i + 1
    right = 2 * i + 2

    if left < n and arr[left] > arr[largest]:
        largest = left

    if right < n and arr[right] > arr[largest]:
        largest = right

    if largest != i:
        arr[i], arr[largest] = arr[largest], arr[i]
        heapify(arr, n, largest)

def heapsort(arr):
    n = len(arr)

    for i in range(n // 2 - 1, -1, -1):
        heapify(arr, n, i)

    for i in range(n - 1, 0, -1):
        arr[i], arr[0] = arr[0], arr[i]
        heapify(arr, i, 0)

# Modified Quicksort Implementation with Randomized Pivot
def partition(arr, low, high):
    pivot_index = random.randint(low, high)
    arr[pivot_index], arr[high] = arr[high], arr[pivot_index]
    pivot = arr[high]

    i = low - 1
    for j in range(low, high):
        if arr[j] <= pivot:
            i += 1
            arr[i], arr[j] = arr[j], arr[i]
    arr[i + 1], arr[high] = arr[high], arr[i + 1]
    return i + 1

def quicksort(arr, low, high):
    if low < high:
        pi = partition(arr, low, high)
        quicksort(arr, low, pi - 1)
        quicksort(arr, pi + 1, high)

def quicksort_wrapper(arr):
    quicksort(arr, 0, len(arr) - 1)

# Merge Sort Implementation
def merge(arr, l, m, r):
    n1 = m - l + 1
    n2 = r - m
    L = [0] * n1
    R = [0] * n2
    for i in range(n1):
        L[i] = arr[l + i]
    for j in range(n2):
        R[j] = arr[m + 1 + j]
    i = 0
    j = 0
    k = l
    while i < n1 and j < n2:
        if L[i] <= R[j]:
            arr[k] = L[i]
            i += 1
        else:
            arr[k] = R[j]
            j += 1
        k += 1
    while i < n1:
        arr[k] = L[i]
        i += 1
        k += 1
    while j < n2:
        arr[k] = R[j]
        j += 1
        k += 1

def mergesort(arr, l, r):
    if l < r:
        m = l + (r - l) // 2
        mergesort(arr, l, m)
        mergesort(arr, m + 1, r)
        merge(arr, l, m, r)

def mergesort_wrapper(arr):
    mergesort(arr, 0, len(arr) - 1)

# Measure time
def measure_time(sort_func, arr):
    start = time.time()
    sort_func(arr)
    return time.time() - start

# Helper to generate different types of arrays
def generate_arrays(n):
    random_array = [random.randint(1, n) for _ in range(n)]
    sorted_array = sorted(random_array)
    reverse_sorted_array = sorted_array[::-1]
    repeated_elements_array = [random.randint(1, 10) for _ in range(n)] 
    return random_array, sorted_array, reverse_sorted_array, repeated_elements_array

# Main function to run comparisons
def run_experiments():
    sizes = [1000, 5000, 10000]
    for size in sizes:
        print(f"Array Size: {size}")
        random_array, sorted_array, reverse_sorted_array, repeated_elements_array = generate_arrays(size)

        # Random array case
        print("Test Case: Random")
        print(f"Heapsort Time: {measure_time(heapsort, random_array[:]):.6f} seconds")
        print(f"Quicksort Time: {measure_time(quicksort_wrapper, random_array[:]):.6f} seconds")
        print(f"Merge Sort Time: {measure_time(mergesort_wrapper, random_array[:]):.6f} seconds")

        # Sorted array case
        print("Test Case: Sorted")
        print(f"Heapsort Time: {measure_time(heapsort, sorted_array[:]):.6f} seconds")
        print(f"Quicksort Time: {measure_time(quicksort_wrapper, sorted_array[:]):.6f} seconds")
        print(f"Merge Sort Time: {measure_time(mergesort_wrapper, sorted_array[:]):.6f} seconds")

        # Reverse sorted array case
        print("Test Case: Reverse Sorted")
        print(f"Heapsort Time: {measure_time(heapsort, reverse_sorted_array[:]):.6f} seconds")
        print(f"Quicksort Time: {measure_time(quicksort_wrapper, reverse_sorted_array[:]):.6f} seconds")
        print(f"Merge Sort Time: {measure_time(mergesort_wrapper, reverse_sorted_array[:]):.6f} seconds")

        # Array with repeated elements
        print("Test Case: Repeated Elements")
        print(f"Heapsort Time: {measure_time(heapsort, repeated_elements_array[:]):.6f} seconds")
        print(f"Quicksort Time: {measure_time(quicksort_wrapper, repeated_elements_array[:]):.6f} seconds")
        print(f"Merge Sort Time: {measure_time(mergesort_wrapper, repeated_elements_array[:]):.6f} seconds")

if __name__ == "__main__":
    run_experiments()
