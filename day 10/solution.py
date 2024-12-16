directions = [
    (0,1), (1,0), (0,-1), (-1,0)
]
def part1():
    grid = []
    with open("input.txt", "r") as file:
        grid = [list(line.strip()) for line in file]

    valid_trailheads= set([])

    def find_path(f_r, f_c, c_r, c_c, c_val):

        if int(grid[c_r][c_c]) == 9:
            valid_trailheads.add((f_r, f_c, c_r, c_c))
            return
        
        for dr, dc in directions:
            n_r = c_r + dr
            n_c = c_c + dc
            n_val = c_val + 1
        
            if 0 > n_r or n_r >= len(grid) or 0 > n_c or n_c >= len(grid[0]):
                continue
            
            if int(grid[n_r][n_c]) == n_val:
                find_path(f_r, f_c, n_r, n_c, n_val)
        

    rows = len(grid)
    cols = len(grid[0])

    for r in range(rows):
        for c in range(cols):
            if grid[r][c] == '0':
                find_path(r,c,r,c,0)

    return len(valid_trailheads)

def part2():
    grid = []
    with open("input.txt", "r") as file:
        grid = [list(line.strip()) for line in file]

    valid_path = []

    def find_path(c_r, c_c, c_val, path):

        if int(grid[c_r][c_c]) == 9:
            valid_path.append(path)
            return
        
        for dr, dc in directions:
            n_r = c_r + dr
            n_c = c_c + dc
            n_val = c_val + 1
        
            if 0 > n_r or n_r >= len(grid) or 0 > n_c or n_c >= len(grid[0]):
                continue
            
            if int(grid[n_r][n_c]) == n_val:
                path.append((n_r, n_c))
                find_path(n_r, n_c, n_val, path)
        

    rows = len(grid)
    cols = len(grid[0])

    for r in range(rows):
        for c in range(cols):
            if grid[r][c] == '0':
                path = [(r, c)]
                find_path(r,c,0, path)

    return len(valid_path)

    
if __name__ == "__main__":
    print("part 1 " + str(part1()))
    print("part 2 " + str(part2()))