def recursiveFunction(result, nums, index = 1, current_val = None):
    if current_val is None:
        current_val = nums[0]

    if index == len(nums):
        return current_val == result
    
    add_res = recursiveFunction(result, nums, index + 1, current_val + nums[index])
    multiply_res = recursiveFunction(result, nums, index + 1, current_val * nums[index])

    return add_res or multiply_res

def part1():
    answer = 0
    equations = []
    main = []
    with open("input.txt", "r") as file:
        equations = list(line.strip().split(':')for line in file)
    
    for first, second in equations:
        res = int(first)
        nums = [int(x) for x in second.strip().split()]
        main.append([res, nums])
    
    for line in main:
        if recursiveFunction(line[0], line[1]):
            answer += line[0]
    return answer

def recursiveFunctionWithConcat(result, nums, index = 1, current_val = None):
    if current_val is None:
        current_val = nums[0]

    if index == len(nums):
        return current_val == result
    
    add_res = recursiveFunctionWithConcat(result, nums, index + 1, current_val + nums[index])
    multiply_res = recursiveFunctionWithConcat(result, nums, index + 1, current_val * nums[index])
    concat_res = recursiveFunctionWithConcat(result, nums, index + 1, int(str(current_val) + str(nums[index])))

    return add_res or multiply_res or concat_res

def part2():
    answer = 0
    equations = []
    main = []
    with open("input.txt", "r") as file:
        equations = list(line.strip().split(':')for line in file)
    
    for first, second in equations:
        res = int(first)
        nums = [int(x) for x in second.strip().split()]
        main.append([res, nums])
    
    for line in main:
        if recursiveFunctionWithConcat(line[0], line[1]):
            answer += line[0]
    return answer

if __name__ == "__main__":
    print("part 1 " + str(part1()))
    print("part 2 " + str(part2()))