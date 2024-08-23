# l1 = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
l1 = list(map(int, input("Enter a list of numbers: ").split()))
l1.sort()
num = int(input("Enter a number: "))
flag = False
low = 0
high = len(l1) - 1
while low <= high:
    mid = (low + high) // 2
    if l1[mid] == num:
        flag = True
        break
    elif l1[mid] < num:
        low = mid + 1
    else:
        high = mid - 1
if flag:
    print(f"Number {num} found at {mid}")
else:
    print(f"Number {num} not found")
    