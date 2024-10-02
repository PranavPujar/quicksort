import random

def quicksort_random(arr):
    if len(arr) <= 1:
        return arr
    else:
        pivot = random.choice(arr)
        left = [x for x in arr if x < pivot]
        middle = [x for x in arr if x == pivot]
        right = [x for x in arr if x > pivot]
        return quicksort_random(left) + middle + quicksort_random(right)

# Helper function for in-place sorting
def quicksort_random_inplace(arr, low, high):
    if low < high:
        pivot_index = random_partition(arr, low, high)
        quicksort_random_inplace(arr, low, pivot_index - 1)
        quicksort_random_inplace(arr, pivot_index + 1, high)

def random_partition(arr, low, high):
    random_pivot = random.randint(low, high)
    arr[random_pivot], arr[high] = arr[high], arr[random_pivot]
    return partition(arr, low, high)

def partition(arr, low, high):
    pivot = arr[high]
    i = low - 1
    for j in range(low, high):
        if arr[j] <= pivot:
            i += 1
            arr[i], arr[j] = arr[j], arr[i]
    arr[i + 1], arr[high] = arr[high], arr[i + 1]
    return i + 1

# Wrapper function for easier use
def quicksort_random_wrapper(arr):
    quicksort_random_inplace(arr, 0, len(arr) - 1)
    return arr