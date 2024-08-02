# given a non empty array of integers nums, every element appears twice except for one. Find that single one.

nums = [1,1,2,2,3,4,4]

nums.sort()

for x in nums:
    if nums.count(x) == 1:
        print(x)
        break