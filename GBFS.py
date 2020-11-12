import copy
import time
# create a class GBFS with attributes (maybe later)

open_list = []
closed_list = []
search_Path = []
solution_file_data = []
search_file_data = []

def search_node():
    return

def choose_heuristic(heuristic_number):
    if heuristic_number == 1:
        [i.apply_heuristic_1() for i in open_list]
    elif heuristic_number == 2:
        [i.apply_heuristic_2() for i in open_list]
    else:
        [i.apply_heuristic_0() for i in open_list]
        
    print([i.get_h() for i in open_list])

def find_children_nodes(node, heuristic_number):
    global open_list, closed_list
    open_list.append(copy.deepcopy(node).move_left())
    open_list.append(copy.deepcopy(node).move_right())
    open_list.append(copy.deepcopy(node).move_down())
    open_list.append(copy.deepcopy(node).move_up())
    # open_list.append(copy.deepcopy(node).wrap_left())
    # open_list.append(node.wrap_right())
    # open_list.append(node.wrap_down())
    # open_list.append(node.wrap_up())
    # open_list.append(node.move_diag_down_left())
    # open_list.append(node.move_diag_down_right())
    # open_list.append(node.move_diag_up_left())
    # open_list.append(node.move_diag_up_right())
    # open_list.append(node.wrap_diag_down_left())
    # open_list.append(node.wrap_diag_down_right())
    # open_list.append(node.wrap_diag_up_left())
    # open_list.append(node.wrap_diag_up_right())
    
    open_list = list(filter(None, open_list))
    choose_heuristic(heuristic_number)
    open_list.sort(key=lambda x: x.get_h())

# Must check if state is already in closed list and open list!
def apply_algorithm(start_node, heuristic_number):
    global open_list, closed_list
    start_time = time.time()
    open_list.append(start_node)
    total_cost = 0
    while(open_list):
        current_node = open_list.pop(0)
        closed_list.append(current_node)
        solution_file_data.append((current_node.get_swapped_token(),
                                   current_node.get_swap_cost(), current_node.get_configuration()))
        search_file_data.append((current_node.get_f(), current_node.get_g(),
                                 current_node.get_h(), current_node.get_configuration()))
        if current_node.is_goal():
            total_cost = current_node.get_g()
            break
        find_children_nodes(current_node, heuristic_number)
        end_time = time.time()
        elapsed_time = end_time - start_time
        if elapsed_time > 60:
            return [], []
        break
    solution_file_data.append((total_cost, elapsed_time))
    print(len(open_list))
    print(len(closed_list))
    
    return solution_file_data, search_file_data