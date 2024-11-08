import random

def print_grid(grid):
    """Utility function to print the 3x3 Sudoku grid."""
    for row in grid:
        print(row)
    print()

def create_sudoku_puzzle():
    """Creates a random 3x3 Sudoku puzzle with some cells empty."""
    # Start with a solved 3x3 grid
    solved_grid = [
        [1, 2, 3],
        [3, 1, 2],
        [2, 3, 1]
    ]
    
    # Randomly remove elements to create a puzzle
    puzzle_grid = [row[:] for row in solved_grid]
    num_cells_to_remove = random.randint(3, 5)  # Random number of cells to remove

    for _ in range(num_cells_to_remove):
        row = random.randint(0, 2)
        col = random.randint(0, 2)
        puzzle_grid[row][col] = 0  # Set cell to 0 (empty)

    return puzzle_grid, solved_grid

def check_solution(user_solution, solved_grid):
    """Check if the user's solution matches the solved grid."""
    return user_solution == solved_grid

# Generate the puzzle and the solution
puzzle, solution = create_sudoku_puzzle()
print("3x3 Sudoku Puzzle (Enter 0 for empty cells):")
print_grid(puzzle)

# Format for answering:
print("Enter your solution in the following format:")
print("Example answer: [[x11, x12, x13], [x21, x22, x23], [x31, x32, x33]]")

# Get user input for their solution
user_input = input("Enter your solution: ")

# Convert user input into a list of lists
try:
    user_solution = eval(user_input)  
except:
    print("Invalid format. Please try again.")

# Check if the user's solution is correct
if check_solution(user_solution, solution):
    print("Congratulations! Your solution is correct.")
else:
    print("Sorry, your solution is incorrect. Here is the correct solution:")
    print_grid(solution)
