# Divide and Conquer

## 4. Searching a Sorted Database

A company has a sorted database containing millions of employee IDs.

### Question

Explain how Binary Search applies the divide-and-conquer concept. What is its time complexity?

### Solution

According to the scenario using the binary search applies the divide and conquer.

### Binary Search applies the Divide-and-Conquer

### Example

Imagine a company has millions of employee IDs, and they are stored in sorted order.

**Employee IDs:**

1001, 1005, 1010, 1015, 1020, 1025, 1030, 1035, 1040

Suppose we want to search = **1025 (target)**

### 1. Divide

* Find the middle element.

**Employee IDs:**

1001, 1005, 1010, 1015, 1020, 1025, 1030, 1035, 1040

**Index:**

0, 1, 2, 3, 4, 5, 6, 7, 8

**Mid calculation:**

mid = (0 + 8) / 2

mid = 4

So,

**mid = 1020**

### 2. Conquer

* Compare the target with the middle value.

**Target = 1025**

**Mid = 1020**

Since:

**1025 > 1020**

Therefore, we know that the target must be on the **right side**.

So, we ignore:

1001, 1005, 1010, 1015, 1020

### 3. Repeat

* Search only the remaining half.

1025, 1030, 1035, 1040

Again, find mid:

mid = (0 + 3) / 2

mid = 1

So,

**mid = 1030**

**Target = 1025**

**Mid = 1030**

Compare:

**1025 < 1030**

Therefore, search the **left half**.

Now:

1025

Compare:

**Target = 1025**

**Mid = 1025**

Therefore:

**1025 Employee ID found.**

# Algorithm

### Input

* Sorted array arr
* Target value target to search

### Steps

1. Set low = 0
2. Set high = len(arr) - 1
3. While low <= high:

   * mid = (low + high) // 2
   * If arr[mid] == target, return the position.
   * If arr[mid] < target, search the right half:

     * low = mid + 1
   * Otherwise, search the left half:

     * high = mid - 1
4. If the loop finishes, the target is not present.

# Python Implementation

```python
def binary_search(arr, target):
    low = 0
    high = len(arr) - 1

    while low <= high:
        mid = (low + high) // 2

        if arr[mid] == target:
            return mid

        elif arr[mid] < target:
            low = mid + 1

        else:
            high = mid - 1

    return -1


employee_ids = [1001, 1005, 1010, 1015, 1020,
                1025, 1030, 1035, 1040]

target = 1025

result = binary_search(employee_ids, target)

if result != -1:
    print("Emp-ID found at index:", result)
else:
    print("Emp-ID not found")
```

# Output

**Emp-ID found at index: 5**

# Time Complexity

### Worst Case

**O(log n)**

### Best Case

**O(1)**


