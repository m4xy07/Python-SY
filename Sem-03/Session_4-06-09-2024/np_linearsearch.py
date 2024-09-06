import numpy as np
arr = np.array([1, 2, 3, 4, 5, 6, 7, 8, 9, 10])
search_value = int(input("Enter value to search"))

found = False
for element in arr:
    if element == search_value:
        found = True
        break

if found:
    print("Element found")
else:
    print("Element not found")