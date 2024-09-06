import numpy as np

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

arr = np.array([2, 4, 6, 8, 10])
target = 6

result = binary_search(arr, target)
if result != -1:
    print("Element found at index", result)
else:
    print("Element not found")  