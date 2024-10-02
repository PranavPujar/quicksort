# Quicksort Implementation and Analysis

This project implements and analyzes two versions of the quicksort algorithm: one with a non-random pivot selection and another with a random pivot selection. It also includes benchmarking code to compare the performance of these algorithms under different scenarios.

## Files in this Project

1. `quicksort.py`: Contains the implementation of quicksort with non-random pivot selection.
2. `quicksort_random.py`: Contains the implementation of quicksort with random pivot selection.
3. `benchmark.py`: Contains code to benchmark the quicksort algorithms and generate performance graphs.

## Answering the Three Questions

### 1. Implementing Quicksort

Two versions of quicksort have been implemented:
- Non-random pivot selection in `quicksort.py`
- Random pivot selection in `quicksort_random.py`

### 2. Benchmarking

The `benchmark.py` file contains code to generate and plot benchmarks for the non-random pivot version of quicksort. It shows:

a) Best case: Using an already sorted array as input.
b) Worst case: Using a reverse-sorted array as input.
c) Average case: Using an array with random elements as input.

The benchmarks are performed for multiple array sizes, and the results are plotted on a single graph.

### 3. Average Runtime Complexity

The average runtime complexity of the non-random pivot version of quicksort is O(n log n). This is derived mathematically as follows:

1. Let T(n) be the time taken by quicksort on an input of size n.
2. In the average case, the pivot divides the array into two roughly equal parts.
3. The recurrence relation is: T(n) = T(n/2) + T(n/2) + cn
4. Solving this recurrence using the recursion tree method:
   - Each level of the tree costs cn
   - There are log₂n levels
5. Therefore, T(n) = cn * log₂n
6. Thus, the average-case time complexity is O(n log n)

## Running the Code

To run the benchmarks and generate the graph:

```
python benchmark.py
```

This will create a file named `quicksort_benchmark.png` with the performance graph.