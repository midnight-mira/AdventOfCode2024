from collections import deque

directions = [
    (1,0), (0,1), (-1,0), (0,-1)
]
def part1():
    grid = []
    with open("input.txt") as file:
        grid = [list(line.strip()) for line in file]

    visited = set([])

    def find_plot(row, col):
        current_plot = deque([])
        current_plot.append((row, col))

        plot_size = 0
        plot_perimeter = 0

        while len(current_plot) > 0:
            c_r, c_c = current_plot.popleft()

            if (c_r, c_c) in visited:
                continue

            visited.add((c_r, c_c))
            plot_size += 1

            for dr, dc in directions:
                n_r, n_c = c_r + dr, c_c + dc

                if n_r < 0 or n_r >= len(grid) or n_c < 0 or n_c >= len(grid[0]):
                    plot_perimeter += 1
                    continue

                if grid[c_r][c_c] != grid[n_r][n_c]:
                    plot_perimeter += 1
                    continue

                if (n_r, n_c) in visited:
                    continue

                current_plot.append((n_r, n_c))

        return plot_perimeter * plot_size
    
    total_plot = 0
    
    for r in range(len(grid)):
        for c in range(len(grid[0])):
            if grid[r][c] not in visited:
                total_plot += find_plot(r, c)
    
    return total_plot

def part2():
    grid = []
    directions = [[-1,0], [0,1], [1,0], [0, -1]]
    visited = set([])

    def inside(row, col):
        return 0 <= row and row < len(grid) and 0<= col and col <len(grid[0])

    def dfs(row, col):

        visited.add((row, col))
        area  = 1
        perimeter = 0

        def good(dir):
            r2, c2 = row + dir[0], col + dir[1]
            return inside(r2,c2) and grid[r2][c2] == grid[row][col]
        
        for i in range(4):
            dir1 = directions[i]
            dir2 = directions[(i+1) %4]
            if(not good(dir1) and not good(dir2)):
                perimeter += 1

            dir_next = dir1[0] + dir2[0], dir1[1] + dir2[1]

            if good(dir1) and good(dir2) and not good(dir_next):
                perimeter += 1

        for dir in directions:
            r2 , c2 = row + dir[0], col + dir[1]
            if good(dir) and (r2,c2) not in visited:
                t_area , t_perimeter = dfs(r2,c2)
                area += t_area
                perimeter += t_perimeter


        return area, perimeter

    
    with open("input.txt") as file:
        grid = [list(line.strip()) for line in file]
        answer =0
        for row in range(len(grid)):
            for col in range(len(grid[0])):
                if (row, col) not in visited:
                    area, perimeter = dfs(row, col)
                    answer += area * perimeter

    return answer


if __name__ == "__main__":
    print("part 1 " + str(part1()))
    print("part 2 " + str(part2()))