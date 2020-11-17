"""
File name:     A_Star.py
Authors:       Maximilien Fathi, Zihan Zhou
Date:          November 16, 2020
Description:   Code used for the application of the A* algorithm.
"""

from copy import deepcopy
import time

"""Global variables."""
open_list = []
closed_list = []
solution_file_data = []
search_file_data = []
closed_list_cost = []


# new
def reset_goblal_variables():
    global open_list, closed_list, solution_file_data, search_file_data,closed_list_cost
    open_list = []
    closed_list = []
    solution_file_data = []
    search_file_data = []
    closed_list_cost = []


def update_solution_file_data(goal_node):
    """Fills solution_file_data list with data related to the ancestors of the goal node."""
    global solution_file_data
    path = goal_node.get_ancestors()
    solution_file_data.append((0, 0, path[0][2]))
    for i in range(0, len(path) - 1):
        solution_file_data.append((path[i][0], path[i][1], path[i - 1][2]))
    solution_file_data.append((path[len(path) - 1][0], path[len(path) - 1][1], goal_node.get_configuration()))

def update_search_file_data(current_node):
    """Fills search_file_data list with data related to the current node."""
    global search_file_data

    search_file_data.append((current_node.get_f(), current_node.get_g(),
                             current_node.get_h(), current_node.get_configuration()))


def choose_heuristic(heuristic_number):
    """Applies correct heuristic method based on what was chosen."""
    if heuristic_number == 1:
        for i in open_list:
            i.apply_heuristic_1()
            i.determine_f()
    elif heuristic_number == 2:
        for i in open_list:
            i.apply_heuristic_2()
            i.determine_f()
    else:
        for i in open_list:
            i.apply_heuristic_0()
            i.determine_f()


def find_children_nodes(node, heuristic_number):
    """Appends children nodes to open list then sorts it accordingly."""
    global open_list, closed_list, closed_list_cost
    configuration = node.get_configuration()
    open_list.append(deepcopy(node).move_left(configuration))
    open_list.append(deepcopy(node).move_right(configuration))
    open_list.append(deepcopy(node).move_down(configuration))
    open_list.append(deepcopy(node).move_up(configuration))
    open_list.append(deepcopy(node).wrap_horizontal(configuration))
    open_list.append(deepcopy(node).wrap_vertical(configuration))
    open_list.append(deepcopy(node).move_diag(configuration))
    open_list.append(deepcopy(node).wrap_diag(configuration))

    # Remove None objects and then sort open list with lowest f first
    open_list = list(filter(None, open_list))
    choose_heuristic(heuristic_number)
    open_list.sort(key=lambda x: x.get_f())
    # Remove duplicates nodes in open list
    temp_list = []
    temp_configuration = []
    for i in range(len(open_list)):
        if (open_list[i].get_configuration() not in temp_configuration) and (
                open_list[i].get_configuration() not in closed_list):
            temp_configuration.append(open_list[i].get_configuration())
            temp_list.append(open_list[i])
        elif open_list[i].get_configuration() in closed_list:
            '''
                If it is found in closed list with a lower cost, as it is in the if statement
                we need to place it in the open_list and do a back track.
            '''
            index = closed_list.index(open_list[i].get_configuration())

            if open_list[i].get_g() < closed_list_cost[index]:
                temp_configuration.append(open_list[i].get_configuration())
                temp_list.append(open_list[i])
                closed_list_cost.pop(index)
                closed_list.pop(index)
    open_list = temp_list


def apply_algorithm(start_node, heuristic_number):
    """Applies the A* algorithm given a start node."""
    global open_list, closed_list, closed_list_cost
    start_time = time.time()
    reset_goblal_variables()  # new
    if heuristic_number == 1:
        start_node.apply_heuristic_1()
        start_node.determine_f()
    elif heuristic_number == 2:
        start_node.apply_heuristic_2()
        start_node.determine_f()
    else:
        start_node.apply_heuristic_0()
        start_node.determine_f()
    open_list.append(start_node)
    total_cost = 0
    elapsed_time = 0
    while open_list:
        current_node = open_list.pop(0)
        configuration = current_node.get_configuration()
        # new
        if configuration in closed_list:
            index = closed_list.index(configuration)
            if current_node.get_g() >= closed_list_cost[index]:
                continue
            else:
                closed_list_cost.pop(index)
                closed_list.pop(index)

        closed_list.append(configuration)
        closed_list_cost.append(current_node.get_g())
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
            return -1, -1, [], []
    solution_file_data.append((total_cost, elapsed_time))
    return elapsed_time, total_cost, solution_file_data, search_file_data
