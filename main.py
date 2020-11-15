"""
File name:     main.py
Authors:       Maximilien Fathi, Zihan Zhou
Date:          November 16, 2020
Description:   Driver file used to run the whole program.
"""

from data_Export import generate_random_puzzles_file, generate_solution_file, generate_search_file
from puzzle import Puzzle
import UCS
import GBFS
import A_Star

def main():
    
    # Variables to change when testing
    #---------------------------------
    number_of_puzzles = 2
    goal_state_1 = [1, 2, 3, 4, 5, 6, 7, 0]
    goal_state_2 = [1, 3, 5, 7, 2, 4, 6, 0]
    row_length = 4
    column_length = 2
    
    test_config = [1, 2, 3, 4, 5, 6, 0, 7] # complex => [0, 7, 2, 5, 4, 6, 3, 1] MORE complex => [0, 3, 7, 5, 2, 6, 4, 1]
    #-----------------------------
    
    # Generate random puzzle configurations
    input_data = generate_random_puzzles_file(number_of_puzzles, test_config, row_length, column_length)
    print(input_data)
    
    # Create a list of puzzle objects
    puzzles = [Puzzle(i, goal_state_1, goal_state_2, row_length, column_length) for i in input_data]
        
    # Apply UCS algorithm on puzzles
    for i in puzzles:
        print(i.get_configuration())
        solution_file_data, search_file_data = UCS.apply_algorithm(i)
        print(solution_file_data)
        generate_solution_file(solution_file_data, puzzles.index(i), "ucs", "")
        generate_search_file(search_file_data, puzzles.index(i), "ucs", "")
    
    # Apply GBFS algorithm (heuristic 1) on puzzles
    heuristic = 1
    for i in puzzles:
        solution_file_data, search_file_data = GBFS.apply_algorithm(i, heuristic)
        generate_solution_file(solution_file_data, puzzles.index(i), "GBFS", f"-h{heuristic}")
        generate_search_file(search_file_data, puzzles.index(i), "GBFS", f"-h{heuristic}")
        
    # Apply GBFS algorithm (heuristic 2) on puzzles
    heuristic = 2
    for i in puzzles:
        solution_file_data, search_file_data = GBFS.apply_algorithm(i, heuristic)
        generate_solution_file(solution_file_data, puzzles.index(i), "GBFS", f"-h{heuristic}")
        generate_search_file(search_file_data, puzzles.index(i), "GBFS", f"-h{heuristic}")
        
    # Apply A* algorithm (heuristic 1) on puzzles
    heuristic = 1
    for i in puzzles:
        solution_file_data, search_file_data = A_Star.apply_algorithm(i, heuristic)
        generate_solution_file(solution_file_data, puzzles.index(i), "astar", f"-h{heuristic}")
        generate_search_file(search_file_data, puzzles.index(i), "astar", f"-h{heuristic}")
        
    # Apply A* algorithm (heuristic 2) on puzzles
    heuristic = 2
    for i in puzzles:
        solution_file_data, search_file_data = A_Star.apply_algorithm(i, heuristic)
        generate_solution_file(solution_file_data, puzzles.index(i), "astar", f"-h{heuristic}")
        generate_search_file(search_file_data, puzzles.index(i), "astar", f"-h{heuristic}")
        
    #--------------------------------------------------------------------------------------------------
    # The following is to be used for the DEMO
    
    # Apply GBFS algorithm (heuristic 0) on puzzles
    heuristic = 0
    for i in puzzles:
        solution_file_data, search_file_data = GBFS.apply_algorithm(i, heuristic)
        generate_solution_file(solution_file_data, puzzles.index(i), "GBFS", f"-h{heuristic}")
        generate_search_file(search_file_data, puzzles.index(i), "GBFS", f"-h{heuristic}")
        
    # Apply A* algorithm (heuristic 0) on puzzles
    heuristic = 0
    for i in puzzles:
        solution_file_data, search_file_data = A_Star.apply_algorithm(i, heuristic)
        generate_solution_file(solution_file_data, puzzles.index(i), "astar", f"-h{heuristic}")
        generate_search_file(search_file_data, puzzles.index(i), "astar", f"-h{heuristic}")
    #--------------------------------------------------------------------------------------------------
    
if __name__ == "__main__":
    main()
