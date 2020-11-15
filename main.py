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
from analysing import analysing

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
    input_data = [[3, 1, 5, 0, 7, 6, 2, 4], [1, 3, 7, 5, 6, 4, 0, 2]]
    puzzles = [Puzzle(i, goal_state_1, goal_state_2, row_length, column_length) for i in input_data]

    UCS_analysis = analysing(number_of_puzzles)
    # Apply UCS algorithm on puzzles
    for i in puzzles:
        time, cost, solution_file_data, search_file_data = UCS.apply_algorithm(i)
        solution_length = generate_solution_file(solution_file_data, puzzles.index(i), "ucs", "")
        search_length = generate_search_file(search_file_data, puzzles.index(i), "ucs", "")
        if (time != -1) and (cost != -1):
            UCS_analysis.add_search_length(search_length)
            UCS_analysis.add_time(time)
            UCS_analysis.add_cost(cost)
            UCS_analysis.add_solution_length(solution_length)
        else:
            UCS_analysis.add_no_solution()

    # Apply GBFS algorithm (heuristic 1) on puzzles
    heuristic = 1
    GBPS_h1_analysis = analysing(number_of_puzzles)
    for i in puzzles:
        time, cost, solution_file_data, search_file_data = GBFS.apply_algorithm(i, heuristic)
        solution_length = generate_solution_file(solution_file_data, puzzles.index(i), "GBFS", f"-h{heuristic}")
        search_length = generate_search_file(search_file_data, puzzles.index(i), "GBFS", f"-h{heuristic}")
        if (time != -1) and (cost != -1):
            GBPS_h1_analysis.add_search_length(search_length)
            GBPS_h1_analysis.add_time(time)
            GBPS_h1_analysis.add_cost(cost)
            GBPS_h1_analysis.add_solution_length(solution_length)
        else:
            GBPS_h1_analysis.add_no_solution()
        
    # Apply GBFS algorithm (heuristic 2) on puzzles
    heuristic = 2
    GBPS_h2_analysis = analysing(number_of_puzzles)
    for i in puzzles:
        time, cost, solution_file_data, search_file_data = GBFS.apply_algorithm(i, heuristic)
        solution_length = generate_solution_file(solution_file_data, puzzles.index(i), "GBFS", f"-h{heuristic}")
        search_length = generate_search_file(search_file_data, puzzles.index(i), "GBFS", f"-h{heuristic}")
        if (time != -1) and (cost != -1):
            GBPS_h2_analysis.add_search_length(search_length)
            GBPS_h2_analysis.add_time(time)
            GBPS_h2_analysis.add_cost(cost)
            GBPS_h2_analysis.add_solution_length(solution_length)
        else:
            GBPS_h2_analysis.add_no_solution()

    # Apply A* algorithm (heuristic 1) on puzzles
    heuristic = 1
    AStar_h1_analysis = analysing(number_of_puzzles)
    for i in puzzles:
        time, cost, solution_file_data, search_file_data = A_Star.apply_algorithm(i, heuristic)
        solution_length = generate_solution_file(solution_file_data, puzzles.index(i), "astar", f"-h{heuristic}")
        search_length = generate_search_file(search_file_data, puzzles.index(i), "astar", f"-h{heuristic}")
        if (time != -1) and (cost != -1):
            AStar_h1_analysis.add_search_length(search_length)
            AStar_h1_analysis.add_time(time)
            AStar_h1_analysis.add_cost(cost)
            AStar_h1_analysis.add_solution_length(solution_length)
        else:
            AStar_h1_analysis.add_no_solution()

    print('total cost of h1:',AStar_h1_analysis.get_cost())
    no_solution = AStar_h1_analysis.get_no_solution()
    print('average cost of h1:', AStar_h1_analysis.get_cost()/(number_of_puzzles - no_solution))
    print('total time of h1:', AStar_h1_analysis.get_time())
    print('average time of h1:', AStar_h1_analysis.get_time() / (number_of_puzzles - no_solution))
    print('total length of solution h1:', AStar_h1_analysis.get_solution_length())
    print('total length of search h1:', AStar_h1_analysis.get_search_length())

    # Apply A* algorithm (heuristic 2) on puzzles
    heuristic = 2
    AStar_h2_analysis = analysing(number_of_puzzles)
    for i in puzzles:
        time, cost, solution_file_data, search_file_data = A_Star.apply_algorithm(i, heuristic)
        solution_length = generate_solution_file(solution_file_data, puzzles.index(i), "astar", f"-h{heuristic}")
        search_length = generate_search_file(search_file_data, puzzles.index(i), "astar", f"-h{heuristic}")
        if (time != -1) and (cost != -1):
            AStar_h2_analysis.add_search_length(search_length)
            AStar_h2_analysis.add_time(time)
            AStar_h2_analysis.add_cost(cost)
            AStar_h2_analysis.add_solution_length(solution_length)
        else:
            AStar_h2_analysis.add_no_solution()



    #--------------------------------------------------------------------------------------------------
    # The following is to be used for the DEMO
    '''
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
    '''
if __name__ == "__main__":
    main()
