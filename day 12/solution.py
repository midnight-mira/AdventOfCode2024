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


if __name__ == "__main__":
    print("part 1 " + str(part1()))