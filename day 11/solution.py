from functools import cache
## can be solved using brute or memoization
def rules(stone):
    if stone == 0:
        return [1]
    if len(str(stone)) % 2 == 0:
        stone_str = str(stone)
        stone_len = len(stone_str)
        return [int(stone_str[:(stone_len//2)]), int(stone_str[(stone_len//2):])]
    
    return [stone * 2024]

@cache
def count_stones(stone, blink):
    if blink == 0:
        return 1
    
    total_stones = 0
    for current_stone in rules(stone):
        total_stones += count_stones(current_stone, blink-1)

    return total_stones


def part1():
    line = ''
    with open("input.txt") as file:
        line = file.readline()

    stones = list(map(int, line.split(' ')))

    for i in range(25):
        temp_stones = []
        for stone in stones:
            temp_stones.extend(rules(stone))
        stones = temp_stones

    return len(stones)

def part2():
    line = ''
    with open("input.txt") as file:
        line = file.readline()

    total_stones = 0
    stones = list(map(int, line.split(' ')))

    for stone in stones:
        total_stones += count_stones(stone, 75)

    return total_stones


if __name__ == "__main__":
    print("part1 "+ str(part1()))
    print("part2 "+ str(part2()))