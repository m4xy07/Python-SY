list_num = map(int, input("Enter numbers sep by space").split())
found = False
for x in list_num:
    if x == num:
        found = True
        break
if found:
    print(f"Number {num} found")
else:
    print(f"Number {num} not found")

