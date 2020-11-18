"""
File name:     main.py
Authors:       Maximilien Fathi, Zihan Zhou
Date:          November 16, 2020
Description:   Driver file used to run the whole program.
"""

from data_Export import generate_random_puzzles_file, read_input_puzzles
from data_Export import generate_search_file, generate_solution_file
from data_Export import generate_analysis_file
from puzzle import Puzzle
import UCS
import GBFS
import A_Star
from analysing import analysing
import numpy
import time

time_list = numpy.zeros(shape = (5, 4))
cost_list = numpy.zeros(shape = (5, 4))

def main():
    global time_list, cost_list
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
    # generate_random_puzzles_file(number_of_puzzles, test_config)
    input_data = read_input_puzzles()

    # complex => [0, 7, 2, 5, 4, 6, 3, 1] MORE complex => [0, 3, 7, 5, 2, 6, 4, 1]
    # input stuff she gave => [[3, 0, 1, 4, 2, 6, 5, 7], [6, 3, 4, 7, 1, 2, 5, 0], [1, 0, 3, 6, 5, 2, 7, 4]]

    # Create a list of puzzle objects
    puzzles = [Puzzle(i, goal_state_1, goal_state_2, row_length, column_length) for i in input_data]

    time_list = numpy.zeros(shape = (5, number_of_puzzles))
    cost_list = numpy.zeros(shape = (5, number_of_puzzles))

    start = time.time()
    UCS_analysis(number_of_puzzles, puzzles)
    print("UCS ends in:", time.time() - start)

    start = time.time()
    GBFS_h1_analysis(number_of_puzzles, puzzles)
    print("GBFS h1 ends in:", time.time() - start)

    start = time.time()
    GBFS_h2_analysis(number_of_puzzles, puzzles)
    print("GBFS h2 ends in:", time.time() - start)

    start = time.time()
    AStar_h1_analysis(number_of_puzzles, puzzles)
    print("Astar h1 ends in:", time.time() - start)

    start = time.time()
    AStar_h2_analysis(number_of_puzzles, puzzles)
    print("Astar h2 ends in:", time.time() - start)

    output_file = f"Output_Files/optimal.txt"
    print(cost_list)
    with open(output_file, 'w') as file_object:
        for i in range(number_of_puzzles):
            optimal = []
            for j in range(0, 5):
                if cost_list[j][i] <= 0.0:
                    time_list[j][i] = 61
                    cost_list[j][i] = 100
                optimal.append(cost_list[j][i])
            min_cost = min(optimal)
            method = []
            while min_cost == min(optimal):
                index = optimal.index(min_cost)
                if index == 0:
                    method.append("UCS")
                elif index == 1:
                    method.append("GBFS with h1")
                elif index == 2:
                    method.append("GBFS with h2")
                elif index == 3:
                    method.append("Astar with h1")
                elif index == 4:
                    method.append("Astar with h2")
                optimal[index] = 100
            file_object.write(f"the optimal path at {i} is {method}")
            file_object.write('\n')

def UCS_analysis(number_of_puzzles, puzzles):
    global time_list, cost_list
    analysis = analysing(number_of_puzzles)
    # Apply UCS algorithm on puzzles
    for i in puzzles:
        time, cost, solution_file_data, search_file_data = UCS.apply_algorithm(i)
        time_list[0][puzzles.index(i)] = time
        cost_list[0][puzzles.index(i)] = cost
        solution_length = generate_solution_file(solution_file_data, puzzles.index(i), "ucs", "")
        search_length = generate_search_file(search_file_data, puzzles.index(i), "ucs", "")
        if (time != -1) and (cost != -1):
            analysis.add_search_length(search_length)
            analysis.add_time(time)
            analysis.add_cost(cost)
            analysis.add_solution_length(solution_length)
        else:
            analysis.add_no_solution()
    generate_analysis_file(analysis, "ucs", "")


def GBFS_h1_analysis(number_of_puzzles, puzzles):
    global time_list, cost_list
    heuristic = 1
    analysis = analysing(number_of_puzzles)
    for i in puzzles:
        time, cost, solution_file_data, search_file_data = GBFS.apply_algorithm(i, heuristic)
        time_list[1][puzzles.index(i)] = time
        cost_list[1][puzzles.index(i)] = cost
        solution_length = generate_solution_file(solution_file_data, puzzles.index(i), "GBFS", f"-h{heuristic}")
        search_length = generate_search_file(search_file_data, puzzles.index(i), "GBFS", f"-h{heuristic}")
        if (time != -1) and (cost != -1):
            analysis.add_search_length(search_length)
            analysis.add_time(time)
            analysis.add_cost(cost)
            analysis.add_solution_length(solution_length)
        else:
            analysis.add_no_solution()
    generate_analysis_file(analysis, "GBFS", f"-h{heuristic}")


def GBFS_h2_analysis(number_of_puzzles, puzzles):
    global time_list, cost_list
    heuristic = 2
    analysis = analysing(number_of_puzzles)
    for i in puzzles:
        time, cost, solution_file_data, search_file_data = GBFS.apply_algorithm(i, heuristic)
        time_list[2][puzzles.index(i)] = time
        cost_list[2][puzzles.index(i)] = cost
        solution_length = generate_solution_file(solution_file_data, puzzles.index(i), "GBFS", f"-h{heuristic}")
        search_length = generate_search_file(search_file_data, puzzles.index(i), "GBFS", f"-h{heuristic}")
        if (time != -1) and (cost != -1):
            analysis.add_search_length(search_length)
            analysis.add_time(time)
            analysis.add_cost(cost)
            analysis.add_solution_length(solution_length)
        else:
            analysis.add_no_solution()
    generate_analysis_file(analysis, "GBFS", f"-h{heuristic}")
    return time_list, cost_list


def AStar_h1_analysis(number_of_puzzles, puzzles):
    global time_list, cost_list
    heuristic = 1
    analysis = analysing(number_of_puzzles)
    for i in puzzles:
        time, cost, solution_file_data, search_file_data = A_Star.apply_algorithm(i, heuristic)
        time_list[3][puzzles.index(i)] = time
        cost_list[3][puzzles.index(i)] = cost
        solution_length = generate_solution_file(solution_file_data, puzzles.index(i), "astar", f"-h{heuristic}")
        search_length = generate_search_file(search_file_data, puzzles.index(i), "astar", f"-h{heuristic}")
        if (time != -1) and (cost != -1):
            analysis.add_search_length(search_length)
            analysis.add_time(time)
            analysis.add_cost(cost)
            analysis.add_solution_length(solution_length)
        else:
            analysis.add_no_solution()
    generate_analysis_file(analysis, "astar", f"-h{heuristic}")
    return time_list, cost_list


def AStar_h2_analysis(number_of_puzzles, puzzles):
    global time_list, cost_list
    heuristic = 2
    analysis = analysing(number_of_puzzles)
    for i in puzzles:
        time, cost, solution_file_data, search_file_data = A_Star.apply_algorithm(i, heuristic)
        time_list[4][puzzles.index(i)] = time
        cost_list[4][puzzles.index(i)] = cost
        solution_length = generate_solution_file(solution_file_data, puzzles.index(i), "astar", f"-h{heuristic}")
        search_length = generate_search_file(search_file_data, puzzles.index(i), "astar", f"-h{heuristic}")
        if (time != -1) and (cost != -1):
            analysis.add_search_length(search_length)
            analysis.add_time(time)
            analysis.add_cost(cost)
            analysis.add_solution_length(solution_length)
        else:
            AStar_h2_analysis.add_no_solution()
    generate_analysis_file(analysis, "astar", f"-h{heuristic}")
    return time_list, cost_list


if __name__ == "__main__":
    main()
