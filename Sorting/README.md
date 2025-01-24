# Sorting Algorithms

## Selection Sort Algorithm
**Selection Sort** is a simple comparison-based sorting algorithm that works by dividing the input list into two parts: the sorted part and the unsorted part.

The algorithm repeatedly finds the minimum (or maximum, depending on the sorting order) element from the unsorted part and swaps it with the first element of the unsorted part. This process is repeated until the entire list becomes sorted.
### Link to the article on Selection Sort:
[Breaking It Down: Understanding Selection Sort with Python](https://medium.com/@basubinayak05/sorting-selection-sort-e92ee3cf64a)

### Note of Stability
**Selection sort is not a stable sorting algorithm**. 

#### Stability in Sorting:
A sorting algorithm is said to be **stable** if it preserves the relative order of records with equal keys (i.e., values that are considered equal remain in the same relative positions after sorting).

#### Why Selection Sort is Not Stable:
In selection sort, swapping is done to place the minimum element in the correct position. This can disrupt the relative order of elements with equal values because:
1. The algorithm searches for the minimum element in the unsorted part of the array.
2. Once the minimum element is found, it swaps it with the first unsorted element, even if that swap changes the order of equal elements.

#### Example Illustrating Instability:
Consider the array:
```python
arr = [(3, 'A'), (3, 'B'), (1, 'C')]
```
Here, the first element of each tuple is the key to be sorted, and the second element represents some additional information.

##### Selection Sort Steps:
1. The algorithm selects `(1, 'C')` as the smallest element and swaps it with `(3, 'A')`:
   ```
   [(1, 'C'), (3, 'B'), (3, 'A')]
   ```
   The relative order of `(3, 'A')` and `(3, 'B')` is now disrupted.

##### Conclusion:
Selection sort may reorder equal elements, making it an **unstable** sorting algorithm. 

#### For Stable Sorting:
Algorithms like **merge sort**, **bubble sort**, or **insertion sort** are stable and maintain the relative order of equal elements.

---

## 