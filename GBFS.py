"""
File name:     GBFS.py
Authors:       Maximilien Fathi, Zihan Zhou
Date:          November 16, 2020
Description:   Code used for the application of the GBFS algorithm.
"""

import copy
import time

"""Global variables."""
open_list = []
closed_list = []  # new
solution_file_data = []
search_file_data = []


def update_solution_file_data(goal_node):
    """Fills solution_file_data list with data related to the ancestors of the goal node."""
    global solution_file_data
    for i in goal_node.get_ancestors():
        solution_file_data.append((i.get_swapped_token(), i.get_swap_cost(),
                                   i.get_configuration()))


def update_search_file_data(current_node):
    """Fills search_file_data list with data related to the current node."""
    global search_file_data
    search_file_data.append((0, 0, current_node.get_h(), current_node.get_configuration()))
    # Different from Kevin's stuff


def choose_heuristic(heuristic_number):
    """Applies correct heuristic method based on what was chosen."""
    if heuristic_number == 1:
        [i.apply_heuristic_1() for i in open_list]
    elif heuristic_number == 2:
        [i.apply_heuristic_2() for i in open_list]
    else:
        [i.apply_heuristic_0() for i in open_list]


def find_children_nodes(node, heuristic_number):
    """Appends children nodes to open list then sorts it accordingly."""
    global open_list, closed_list  # new
    open_list.append(copy.deepcopy(node).move_left(copy.deepcopy(node)))
    open_list.append(copy.deepcopy(node).move_right(copy.deepcopy(node)))
    open_list.append(copy.deepcopy(node).move_down(copy.deepcopy(node)))
    open_list.append(copy.deepcopy(node).move_up(copy.deepcopy(node)))
    open_list.append(copy.deepcopy(node).wrap_left(copy.deepcopy(node)))
    open_list.append(copy.deepcopy(node).wrap_right(copy.deepcopy(node)))
    open_list.append(copy.deepcopy(node).wrap_down(copy.deepcopy(node)))
    open_list.append(copy.deepcopy(node).wrap_up(copy.deepcopy(node)))
    open_list.append(copy.deepcopy(node).move_diag_down_left(copy.deepcopy(node)))
    open_list.append(copy.deepcopy(node).move_diag_down_right(copy.deepcopy(node)))
    open_list.append(copy.deepcopy(node).move_diag_up_left(copy.deepcopy(node)))
    open_list.append(copy.deepcopy(node).move_diag_up_right(copy.deepcopy(node)))
    open_list.append(copy.deepcopy(node).wrap_diag_down_left(copy.deepcopy(node)))
    open_list.append(copy.deepcopy(node).wrap_diag_down_right(copy.deepcopy(node)))
    open_list.append(copy.deepcopy(node).wrap_diag_up_left(copy.deepcopy(node)))
    open_list.append(copy.deepcopy(node).wrap_diag_up_right(copy.deepcopy(node)))

    # Remove None objects and then sort open list with lowest h first
    open_list = list(filter(None, open_list))
    choose_heuristic(heuristic_number)
    open_list.sort(key=lambda x: x.get_h())
    # Remove duplicates nodes in open list
    temp_list = []
    temp_configuration = []
    for i in range(len(open_list)):
        if (open_list[i].get_configuration() not in temp_configuration) and (
                open_list[i].get_configuration() not in closed_list):
            temp_configuration.append(open_list[i].get_configuration())
            temp_list.append(open_list[i])
    open_list = temp_list
    # new


def apply_algorithm(start_node, heuristic_number):
    """Applies the GBFS algorithm given a start node."""
    global open_list, closed_list  # new
    start_time = time.time()
    if heuristic_number == 1:
        start_node.apply_heuristic_1()
    elif heuristic_number == 2:
        start_node.apply_heuristic_2()
    else:
        start_node.apply_heuristic_0()
    open_list.append(start_node)
    total_cost = 0
    elapsed_time = 0  # new
    while open_list:
        current_node = open_list.pop(0)
        configuration = current_node.get_configuration()
        if configuration in closed_list:
            continue
        closed_list.append(configuration)  # new
        update_search_file_data(current_node)
        if current_node.is_goal():
            total_cost = current_node.get_g()
            update_solution_file_data(current_node)
            # new
            end_time = time.time()
            elapsed_time = end_time - start_time
            break
        find_children_nodes(current_node, heuristic_number)
        end_time = time.time()
        elapsed_time = end_time - start_time
        if elapsed_time > 60:
            return [], []
    solution_file_data.append((current_node.get_swapped_token(),
                               current_node.get_swap_cost(), current_node.get_configuration()))
    solution_file_data.append((total_cost, elapsed_time))
    return solution_file_data, search_file_data
