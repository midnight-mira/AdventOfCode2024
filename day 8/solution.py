from collections import defaultdict

def part1():
    result = 0
    with open("input.txt", "r") as file:
        grid  = list(map(str.strip, file.readlines()))

    antennas = defaultdict(set)

    rows = len(grid)
    cols = len(grid[0])

    for r, line in enumerate(grid):
        for c, val in enumerate(line):
            if val != '.':
                antennas[val].add((r,c))

    antinodes = set()
    for freq in antennas:
        for (r1, c1) in antennas[freq]:
            for (r2, c2) in antennas[freq]:
                if (r1 != r2) and (c1 != c2):
                    # distance between rows and cols
                    dr , dc = r2 - r1, c2 -c1 
                    antinodes.add((r1 - dr, c1 - dc))
                    antinodes.add((r2 + dr, c2 + dc))

    for r,c in antinodes:
        if 0 <= r < rows and 0 <= c < cols:
            result += 1

    return result

def part2():
    

if __name__ == "__main__":
    print("part 1 " + str(part1()))