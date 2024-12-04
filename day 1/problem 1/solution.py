# Initialize two lists for the columns
left_column = []
right_column = []

# Open and read the file
with open("input.txt", "r") as file:
    for line in file:
        # Split the line into two numbers
        left, right = map(int, line.split())
        # Append the numbers to their respective lists
        left_column.append(left)
        right_column.append(right)

# Print the results
#print("Left Column:", left_column)
#print("Right Column:", right_column)

left_column.sort()
right_column.sort()
distance =0

for i in range(len(left_column)):
    distance +=  abs(left_column[i] - right_column[i])

print(distance)