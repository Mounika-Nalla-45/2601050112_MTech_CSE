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