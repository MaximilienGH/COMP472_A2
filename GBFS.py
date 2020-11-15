"""
File name:     GBFS.py
Authors:       Maximilien Fathi, Zihan Zhou
Date:          November 16, 2020
Description:   Code used for the application of the GBFS algorithm.
"""

from copy import deepcopy
import time

"""Global variables."""
open_list = []
closed_list = []
solution_file_data = []
search_file_data = []

# new
def reset_goblal_variables():
    global open_list, closed_list, solution_file_data, search_file_data  
    open_list = []
    closed_list = []
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
    global open_list, closed_list
    open_list.append(deepcopy(node).move_left(deepcopy(node)))
    open_list.append(deepcopy(node).move_right(deepcopy(node)))
    open_list.append(deepcopy(node).move_down(deepcopy(node)))
    open_list.append(deepcopy(node).move_up(deepcopy(node)))
    open_list.append(deepcopy(node).wrap_left(deepcopy(node)))
    open_list.append(deepcopy(node).wrap_right(deepcopy(node)))
    open_list.append(deepcopy(node).wrap_down(deepcopy(node)))
    open_list.append(deepcopy(node).wrap_up(deepcopy(node)))
    open_list.append(deepcopy(node).move_diag_down_left(deepcopy(node)))
    open_list.append(deepcopy(node).move_diag_down_right(deepcopy(node)))
    open_list.append(deepcopy(node).move_diag_up_left(deepcopy(node)))
    open_list.append(deepcopy(node).move_diag_up_right(deepcopy(node)))
    open_list.append(deepcopy(node).wrap_diag_down_left(deepcopy(node)))
    open_list.append(deepcopy(node).wrap_diag_down_right(deepcopy(node)))
    open_list.append(deepcopy(node).wrap_diag_up_left(deepcopy(node)))
    open_list.append(deepcopy(node).wrap_diag_up_right(deepcopy(node)))

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


def apply_algorithm(start_node, heuristic_number):
    """Applies the GBFS algorithm given a start node."""
    global open_list, closed_list
    start_time = time.time()
    reset_goblal_variables()  # new
    if heuristic_number == 1:
        start_node.apply_heuristic_1()
    elif heuristic_number == 2:
        start_node.apply_heuristic_2()
    else:
        start_node.apply_heuristic_0()
    open_list.append(start_node)
    total_cost = 0
    elapsed_time = 0
    while open_list:
        current_node = open_list.pop(0)
        configuration = current_node.get_configuration()
        # new
        if configuration in closed_list:
            continue
        closed_list.append(configuration)
        update_search_file_data(current_node)
        if current_node.is_goal():
            total_cost = current_node.get_g()
            update_solution_file_data(current_node)
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
