# Open the input file
file = open("input.txt", "r")

def check_adjacent_difference(sequence):
    return all(1 <= abs(sequence[i] - sequence[i + 1] ) <= 3 for i in range(len(sequence) - 1))

def Monotone(sequence):
    return all(sequence[i] < sequence[i + 1] for i in range(len(sequence) - 1)) or \
           all(sequence[i] > sequence[i + 1] for i in range(len(sequence) - 1))

answer = 0
# Read and process each line
for x in file:
    # Convert the line into a list of integers
    numbers = list(map(int, x.strip().split()))
    
    # Check the adjacent level differences
    result = check_adjacent_difference(numbers) and Monotone(numbers)
    
    if result:
        answer += 1
print(answer)

file.close()
