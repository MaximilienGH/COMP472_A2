"""
File name:     main.py
Authors:       Maximilien Fathi, Zihan Zhou
Date:          November 16, 2020
Description:   Driver file used to run the whole program.
"""

from data_Export import generate_solution_file, generate_search_file
from puzzle import Puzzle
import UCS
import GBFS
import A_Star

def main():

    # filename = 'samplePuzzles.txt'
    # with open (filename) as file_object:
    #     for line in file_object:
    #         print(line)
    
    initial_state = [0, 7, 2, 5, 4, 6, 3, 1] # complex => [0, 7, 2, 5, 4, 6, 3, 1]
    goal_state_1 = [1, 2, 3, 4, 5, 6, 7, 0]  # 2x2 => [1, 2, 3, 0]
    goal_state_2 = [1, 3, 5, 7, 2, 4, 6, 0]  # 2x2 => [1, 2, 3, 0]
    
    puzzle = Puzzle(initial_state, goal_state_1, goal_state_2, 4, 2)
    # puzzle = Puzzle([4,2,3,1,5,6,7,0,8], 3, 3)
    # puzzle = Puzzle([3, 1, 0, 2], 2, 2)
    # puzzle = Puzzle([0,8,3,7,6,1,5,2,4], 3, 3)
    
    # solution_file_data, search_file_data = UCS.apply_algorithm(puzzle)
    # generate_solution_file(solution_file_data, 0, "ucs", "")
    # generate_search_file(search_file_data, 0, "ucs", "")
    
    solution_file_data, search_file_data = GBFS.apply_algorithm(puzzle, 1) # 2nd argument is heuristic number
    generate_solution_file(solution_file_data, 0, "GBFS", "-h1")
    generate_search_file(search_file_data, 0, "GBFS", "-h1")
    
    # solution_file_data, search_file_data = A_Star.apply_algorithm(puzzle, 1) # 2nd argument is heuristic number
    # generate_solution_file(solution_file_data, 0, "astar", "-h1")
    # generate_search_file(search_file_data, 0, "astar", "-h1")

if __name__ == "__main__":
    main()
