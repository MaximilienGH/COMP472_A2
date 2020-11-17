"""
File name:     main.py
Authors:       Maximilien Fathi, Zihan Zhou
Date:          November 16, 2020
Description:   Driver file used to run the whole program.
"""

from data_Export import generate_random_puzzles_file, read_input_puzzles
from data_Export import generate_search_file, generate_solution_file
from puzzle import Puzzle
import UCS
import GBFS
import A_Star
import UCS_WITH_PQ
from queue import PriorityQueue
from analysing import analysing


def main():
    # Variables to change when testing
    # ---------------------------------
    number_of_puzzles = 50
    goal_state_1 = [1, 2, 3, 4, 5, 6, 7, 0]
    goal_state_2 = [1, 3, 5, 7, 2, 4, 6, 0]
    row_length = 4
    column_length = 2

    test_config = [1, 2, 3, 4, 5, 6, 0, 7]
    # -----------------------------

    # Generate random puzzle configurations and read them
    generate_random_puzzles_file(number_of_puzzles, test_config)
    input_data = read_input_puzzles()

    #input_data = [[3, 0, 1, 4, 2, 6, 5, 7], [6, 3, 4, 7, 1, 2, 5, 0], [1, 0, 3, 6, 5, 2, 7, 4]]

    # complex => [0, 7, 2, 5, 4, 6, 3, 1] MORE complex => [0, 3, 7, 5, 2, 6, 4, 1]
    # input stuff she gave => [[3, 0, 1, 4, 2, 6, 5, 7], [6, 3, 4, 7, 1, 2, 5, 0], [1, 0, 3, 6, 5, 2, 7, 4]]

    # Create a list of puzzle objects
    puzzles = [Puzzle(i, goal_state_1, goal_state_2, row_length, column_length) for i in input_data]

    #UCS_analysis(number_of_puzzles, puzzles)
    GBFS_h1_analysis(number_of_puzzles, puzzles)
    GBFS_h2_analysis(number_of_puzzles, puzzles)
    AStar_h1_analysis(number_of_puzzles, puzzles)
    AStar_h2_analysis(number_of_puzzles, puzzles)

    # --------------------------------------------------------------------------------------------------
    # # The following is to be used for the DEMO

    # # Apply GBFS algorithm (heuristic 0) on puzzles
    # heuristic = 0
    # for i in puzzles:
    #     solution_file_data, search_file_data = GBFS.apply_algorithm(i, heuristic)
    #     generate_solution_file(solution_file_data, puzzles.index(i), "GBFS", f"-h{heuristic}")
    #     generate_search_file(search_file_data, puzzles.index(i), "GBFS", f"-h{heuristic}")

    # # Apply A* algorithm (heuristic 0) on puzzles
    # heuristic = 0
    # for i in puzzles:
    #     solution_file_data, search_file_data = A_Star.apply_algorithm(i, heuristic)
    #     generate_solution_file(solution_file_data, puzzles.index(i), "astar", f"-h{heuristic}")
    #     generate_search_file(search_file_data, puzzles.index(i), "astar", f"-h{heuristic}")
    # --------------------------------------------------------------------------------------------------


def UCS_analysis(number_of_puzzles, puzzles):
    UCS_analysis = analysing(number_of_puzzles)
    # Apply UCS algorithm on puzzles
    for i in puzzles:
        time, cost, solution_file_data, search_file_data = UCS.apply_algorithm(i)
        solution_length = generate_solution_file(solution_file_data, puzzles.index(i), "ucs", "")
        search_length = generate_search_file(search_file_data, puzzles.index(i), "ucs", "")
        print("Puzzle Number:", puzzles.index(i), "is done with UCS at time of :", time)
        if (time != -1) and (cost != -1):
            UCS_analysis.add_search_length(search_length)
            UCS_analysis.add_time(time)
            UCS_analysis.add_cost(cost)
            UCS_analysis.add_solution_length(solution_length)
        else:
            UCS_analysis.add_no_solution()


def GBFS_h1_analysis(number_of_puzzles, puzzles):
    heuristic = 1
    GBPS_h1_analysis = analysing(number_of_puzzles)
    for i in puzzles:
        time, cost, solution_file_data, search_file_data = GBFS.apply_algorithm(i, heuristic)
        solution_length = generate_solution_file(solution_file_data, puzzles.index(i), "GBFS", f"-h{heuristic}")
        search_length = generate_search_file(search_file_data, puzzles.index(i), "GBFS", f"-h{heuristic}")
        print("Puzzle Number:", puzzles.index(i), "is done with GBFS at time of :", time)
        if (time != -1) and (cost != -1):
            GBPS_h1_analysis.add_search_length(search_length)
            GBPS_h1_analysis.add_time(time)
            GBPS_h1_analysis.add_cost(cost)
            GBPS_h1_analysis.add_solution_length(solution_length)
        else:
            GBPS_h1_analysis.add_no_solution()


def GBFS_h2_analysis(number_of_puzzles, puzzles):
    heuristic = 2
    GBPS_h2_analysis = analysing(number_of_puzzles)
    for i in puzzles:
        time, cost, solution_file_data, search_file_data = GBFS.apply_algorithm(i, heuristic)
        solution_length = generate_solution_file(solution_file_data, puzzles.index(i), "GBFS", f"-h{heuristic}")
        search_length = generate_search_file(search_file_data, puzzles.index(i), "GBFS", f"-h{heuristic}")
        print("Puzzle Number:", puzzles.index(i), "is done with GBFS at time of :", time)
        if (time != -1) and (cost != -1):
            GBPS_h2_analysis.add_search_length(search_length)
            GBPS_h2_analysis.add_time(time)
            GBPS_h2_analysis.add_cost(cost)
            GBPS_h2_analysis.add_solution_length(solution_length)
        else:
            GBPS_h2_analysis.add_no_solution()


def AStar_h1_analysis(number_of_puzzles, puzzles):
    heuristic = 1
    AStar_h1_analysis = analysing(number_of_puzzles)
    for i in puzzles:
        time, cost, solution_file_data, search_file_data = A_Star.apply_algorithm(i, heuristic)
        solution_length = generate_solution_file(solution_file_data, puzzles.index(i), "astar", f"-h{heuristic}")
        search_length = generate_search_file(search_file_data, puzzles.index(i), "astar", f"-h{heuristic}")
        print("Puzzle Number:", puzzles.index(i), "is done with AStar at time of :", time)
        if (time != -1) and (cost != -1):
            AStar_h1_analysis.add_search_length(search_length)
            AStar_h1_analysis.add_time(time)
            AStar_h1_analysis.add_cost(cost)
            AStar_h1_analysis.add_solution_length(solution_length)
        else:
            AStar_h1_analysis.add_no_solution()


def AStar_h2_analysis(number_of_puzzles, puzzles):
    heuristic = 2
    AStar_h2_analysis = analysing(number_of_puzzles)
    for i in puzzles:
        time, cost, solution_file_data, search_file_data = A_Star.apply_algorithm(i, heuristic)
        solution_length = generate_solution_file(solution_file_data, puzzles.index(i), "astar", f"-h{heuristic}")
        search_length = generate_search_file(search_file_data, puzzles.index(i), "astar", f"-h{heuristic}")
        print("Puzzle Number:", puzzles.index(i), "is done with AStar at time of :", time)
        if (time != -1) and (cost != -1):
            AStar_h2_analysis.add_search_length(search_length)
            AStar_h2_analysis.add_time(time)
            AStar_h2_analysis.add_cost(cost)
            AStar_h2_analysis.add_solution_length(solution_length)
        else:
            AStar_h2_analysis.add_no_solution()


if __name__ == "__main__":
    main()
