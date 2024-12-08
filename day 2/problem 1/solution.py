lines  = []
safe =0
with open("input.txt", "r") as file:
    lines = file.readlines()

def isSafe(nums):
    for i in range(len(nums) - 1):
        a, b = nums[i], nums[i+1]
        if not 1 <= abs(a-b) <= 3:
            return False
        if i == len(nums) - 2:
            continue
        c = nums[i+2]
        if not a< b< c and not a > b> c:
             return False
    return True
        
for line in lines:
    numbers = list(map(int, line.split(' ')))
    if isSafe(numbers):
        safe += 1

print(safe)
   

