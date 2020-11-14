"""
File name:     UCS.py
Authors:       Maximilien Fathi, Zihan Zhou
Date:          November 16, 2020
Description:   Code used for the application of the UCS algorithm.
"""

from copy import deepcopy
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
    search_file_data.append((0, current_node.get_g(), 0, current_node.get_configuration()))


def find_children_nodes(node):
    """Appends children nodes to open list then sorts it accordingly."""
    global open_list, closed_list  # new
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

    # Remove None objects and then sort open list with lowest g first
    open_list = list(filter(None, open_list))
    open_list.sort(key=lambda x: x.get_g())
    # Remove duplicates nodes with equal or higher cost in open list
    temp_list = []
    temp_configuration = []
    for i in range(len(open_list)):
        if (open_list[i].get_configuration() not in temp_configuration) and (
                open_list[i].get_configuration() not in closed_list):
            temp_configuration.append(open_list[i].get_configuration())
            temp_list.append(open_list[i])
    open_list = temp_list
    # new


def apply_algorithm(start_node):
    """Applies the UCS algorithm given a start node."""
    global open_list, closed_list  # new
    start_time = time.time()
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
        find_children_nodes(current_node)
        end_time = time.time()
        elapsed_time = end_time - start_time
        if elapsed_time > 60:
            return [], []
    solution_file_data.append((current_node.get_swapped_token(),
                               current_node.get_swap_cost(), current_node.get_configuration()))
    solution_file_data.append((total_cost, elapsed_time))
    return solution_file_data, search_file_data
