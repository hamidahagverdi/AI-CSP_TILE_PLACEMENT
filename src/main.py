"""
This program tackles the Tile Placement challenge by applying Constraint Satisfaction Problem methods. 
It uses a combination of the AC3 algorithm to narrow down possible solutions and backtracking to find the correct arrangement. 

The program starts by loading landscape information from a file, then works to position tiles according to specific constraints.
Once it finds a valid solution, it saves the results to a file. Throughout the process, the program tracks and displays 
how long the calculation took, how many tries it made, and the complete solution.
"""

import time
import sys
import os
from Landscape import Landscape
from Solver import Solver


if __name__ == "__main__":
    print("Solving....")
    
    # Record the start time to measure the execution time
    start_time = time.time()

    # Get the input file path from command-line arguments
    input_file = sys.argv[1]  # Input file containing the landscape data
    output_folder = "output"  # Folder to save the output solution
    os.makedirs(output_folder, exist_ok=True)  # Ensure the output folder exists (create if not)

    # Derive the output file name based on the input file name
    output_file = os.path.join(output_folder, os.path.basename(input_file).replace(".txt", "_solution.txt"))

    # Read the landscape data from the input file
    with open(input_file, 'r') as file:
        landscape_data = file.read()

    # Build the landscape object using the data from the file
    landscape = Landscape.build(landscape_data)

    # Create a solver instance with the built landscape
    solver = Solver(landscape)

    # **Run AC3 (Arc-Consistency) to propagate constraints before performing backtracking**
    # AC3 checks for any immediate inconsistencies in the puzzle that would make it unsolvable
    if not solver.ac3():
        # If no solution is found due to inconsistency, write an appropriate message to the output file
        with open(output_file, 'w') as file:
            file.write(landscape_data + "\n")  # Copy the input data to the output
            file.write("No solution due to inconsistency\n")
        print("No solution due to inconsistency")
        print(f"Solution written to {output_file}")
        sys.exit()  # Exit early since no solution is possible

    # If AC3 passed, proceed to solve the problem using backtracking
    result = solver.backtrack(solver.heuristics.get_mrv())

    # Write the output to the solution file
    with open(output_file, 'w') as file:
        # First, write the original input data to the output file
        file.write(landscape_data + "\n")

        if not result:
            # If no solution was found, mark the result as unsolved
            file.write("Unsolved\n")
            print("Unsolved")
        else:
            # If a solution is found, write the solution details to the output
            file.write("Solution:\n\n")
            # Sort the squares by their index and write the assigned tiles to the file
            for square in sorted(solver.landscape.squares, key=lambda x: x.index):
                file.write(f"{square.index} 4 {square.assigned_tile}\n")

    # Calculate and print the total time taken to solve the problem in milliseconds
    elapsed_time = (time.time() - start_time) * 1000
    print(f"Milliseconds elapsed: {elapsed_time:.2f}")
    print(f"Iterations: {solver.iterations}")  # Print the number of iterations used during backtracking
    print(f"Solution written to {output_file}")
