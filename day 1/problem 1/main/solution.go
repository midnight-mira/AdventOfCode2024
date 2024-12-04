package main

import (
	"bufio"
	"fmt"
	"os"
)

func main() {
	// Open the file
	readFile, err := os.Open("D://advent 2025/day 1/problem 1/input.txt")
	var leftColumn []int
	var rightColumn []int

	// Check for errors when opening the file
	if err != nil {
		fmt.Println("Error opening file:", err)
		return
	}
	defer readFile.Close() // Ensure the file is closed when done

	// Set up the scanner to read the file line by line
	fileScanner := bufio.NewScanner(readFile)

	// Split by lines
	fileScanner.Split(bufio.ScanLines)

	// Read the file line by line
	for fileScanner.Scan() {
		line =: fileScanner.Text()
		// Print each line
		parts := strings.Fields(line)
		if len(parts) == 2 {
			// Parse integers directly from the parts and append them to the columns
			left := parseInteger(parts[0])
			right := parseInteger(parts[1])

			// Append to respective columns
			leftColumn = append(leftColumn, left)
			rightColumn = append(rightColumn, right)
		} else {
			fmt.Println("Invalid line format:", line)
		}
	}

	// Check if there was an error during scanning
	if err := fileScanner.Err(); err != nil {
		fmt.Println("Error reading file:", err)
	}
}
