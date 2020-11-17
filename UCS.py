"""
File name:     UCS.py
Authors:       Maximilien Fathi, Zihan Zhou
Date:          November 16, 2020
Description:   Code used for the application of the UCS algorithm.
"""

from copy import deepcopy
import time
from data_Export import *

"""Global variables."""
open_list = []
closed_list = []
solution_file_data = []
search_file_data = []

def reset_goblal_variables():
    global open_list, closed_list, solution_file_data, search_file_data
    open_list = []
    closed_list = []
    solution_file_data = []
    search_file_data = []


def update_solution_file_data(goal_node):
    """Fills solution_file_data list with data related to the ancestors of the goal node."""
    global solution_file_data
    path = goal_node.get_ancestors()
    solution_file_data.append((0, 0, goal_node.get_initial()))
    for i in range(0, len(path) - 1):
        solution_file_data.append((path[i][0], path[i][1], path[i + 1][2]))
    if len(path) != 0:
        solution_file_data.append((path[len(path) - 1][0], path[len(path) - 1][1], goal_node.get_configuration()))


def update_search_file_data(current_node):
    """Fills search_file_data list with data related to the current node."""
    global search_file_data
    search_file_data.append((0, current_node.get_g(), 0, current_node.get_configuration()))


def find_children_nodes(node):
    """Appends children nodes to open list then sorts it accordingly."""
    global open_list, closed_list
    configuration = node.get_configuration()
    open_list.append(deepcopy(node).move_left(configuration))
    open_list.append(deepcopy(node).move_right(configuration))
    open_list.append(deepcopy(node).move_down(configuration))
    open_list.append(deepcopy(node).move_up(configuration))
    open_list.append(deepcopy(node).wrap_horizontal(configuration))
    open_list.append(deepcopy(node).wrap_vertical(configuration))
    open_list.append(deepcopy(node).move_diag(configuration))
    open_list.append(deepcopy(node).wrap_diag(configuration))

    # Remove None objects and then sort open list with lowest g first
    open_list = list(filter(None, open_list))
    open_list.sort(key=lambda x: x.get_g())
    # Remove duplicates nodes with equal or higher cost in open list
    temp_list = []
    temp_configuration = []
    for i in range(len(open_list)):
        if open_list[i].get_configuration() not in temp_configuration:
            temp_configuration.append(open_list[i].get_configuration())
            temp_list.append(open_list[i])
    open_list = temp_list


def apply_algorithm(start_node):
    """Applies the UCS algorithm given a start node."""
    global open_list, closed_list
    start_time = time.time()
    reset_goblal_variables()  # new
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
        find_children_nodes(current_node)
        end_time = time.time()
        elapsed_time = end_time - start_time
        if elapsed_time > 60:
            return -1, -1, [], []
    solution_file_data.append((total_cost, elapsed_time))
    return elapsed_time, total_cost, solution_file_data, search_file_data
