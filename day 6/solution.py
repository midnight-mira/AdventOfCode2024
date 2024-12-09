


def part1():
    direction = [(-1,0), (0,1), (1,0),(0,-1)]
    lab = []
    directn = 0
    result = set()
    exit = False
    with open("input.txt") as file:
        lab = [list(line.strip()) for line in file]
    
    (current_x, current_y) = (-1, -1)
    rows = len(lab)
    cols = len(lab[0])
    for i in range(rows):
        for j in range(cols):
            if lab[i][j] == "^":
                
                (current_x, current_y) = (i,j)
                lab[i][j] = "."
    
    while not exit:
        result.add((current_x, current_y))
        next_x, next_y = current_x + direction[directn][0], current_y + direction[directn][1]
        if not (0 <= next_x < rows and 0 <= next_y < cols):
            exit = True
            break

        if lab[next_x][next_y] == ".":
            current_x, current_y = next_x, next_y

        else:
            directn = (directn + 1) % 4

    return (len(result))

def part2():

    def solve_cycle(start_x, start_y):
        """Checks if the robot completes a cycle starting from (start_x, start_y)."""
        current_x, current_y = start_x, start_y
        directn = 0  # Initial direction
        visited = set()  # To track visited positions
        turns = 0


        while True:
            # Protect against infinite loops
            turns += 1
            if turns == 10000:
                return True

            visited.add((current_x, current_y, directn))

            # Calculate the next position
            next_x = current_x + direction[directn][0]
            next_y = current_y + direction[directn][1]

            # Check if out of bounds
            if not (0 <= next_x < rows and 0 <= next_y < cols):
                return False

            # If the next cell is a free space, move there
            if lab[next_x][next_y] == ".":
                current_x, current_y = next_x, next_y

            # Otherwise, turn clockwise
            else:
                directn = (directn + 1) % 4


    # Directions: up, right, down, left
    direction = [(-1, 0), (0, 1), (1, 0), (0, -1)]
    lab = []  # Initialize labyrinth
    answer = 0

    # Read the labyrinth from the file
    with open("input.txt") as file:
        lab = [list(line.strip()) for line in file]

    # Find the starting point
    start_x, start_y = -1, -1
    rows, cols = len(lab), len(lab[0])
    for i in range(rows):
        for j in range(cols):
            if lab[i][j] == "^":  # Starting point
                start_x, start_y = i, j
                lab[i][j] = "."  # Replace starting point with a free space

    # Iterate over all free spaces in the labyrinth
    for i in range(rows):
        for j in range(cols):
            if lab[i][j] == "." and (i, j) != (start_x, start_y):
                lab[i][j] = "#"  # Temporarily block this cell
                if solve_cycle(start_x, start_y):  # Check for a cycle
                    answer += 1
                lab[i][j] = "."  # Restore the cell to its original state

    # Print the result
    return answer



if __name__ == "__main__":
    print("part 1 " + str(part1()))
    print("part 2" + str(part2()))


    
   

        

            

                

            



    

    
