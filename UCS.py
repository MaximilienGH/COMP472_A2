import copy
import time
# create a class UCS with attributes (maybe later)

open_list = []
closed_list = []
cL = []
search_Path = []
solution_file_data = []
search_file_data = []

# def search_node():
#     return

def update_solution_file_data(goal_node):
    global solution_file_data
    for i in goal_node.get_ancestors():
        solution_file_data.append((i.get_swapped_token(),
                                   i.get_swap_cost(),
                                   i.get_configuration()))
    
def update_search_file_data(current_node):
    global search_file_data
    search_file_data.append((0,
                             current_node.get_g(),
                             0,
                             current_node.get_configuration()))

def find_children_nodes(node):
    global open_list, cL
    open_list.append(copy.deepcopy(node).move_left(copy.deepcopy(node)))
    open_list.append(copy.deepcopy(node).move_right(copy.deepcopy(node)))
    open_list.append(copy.deepcopy(node).move_down(copy.deepcopy(node)))
    open_list.append(copy.deepcopy(node).move_up(copy.deepcopy(node)))


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


    open_list = list(filter(None, open_list))
    open_list.sort(key=lambda x: x.get_g())
    temp_list = []
    temp_configuration = []
    for i in range(len(open_list)):
        if (open_list[i].get_configuration() not in temp_configuration) and (open_list[i].get_configuration() not in cL):
            temp_configuration.append(open_list[i].get_configuration())
            temp_list.append(open_list[i])
    open_list = temp_list

    print('start point')
    for i in range(len(open_list)):
        print(open_list[i].get_configuration(), (open_list[i].get_g()))
    print("break point")

# Must check if state is already in closed list and open list!
def apply_algorithm(start_node):
    global open_list, closed_list, cL
    start_time = time.time()
    open_list.append(start_node)
    total_cost = 0
    elapsed_time = 0
    while(open_list):
        current_node = open_list.pop(0)
        closed_list.append(current_node)
        cL.append(current_node.get_configuration())
        update_search_file_data(current_node)
        if current_node.is_goal():
            total_cost = current_node.get_g()
            update_solution_file_data(current_node)
            break
        find_children_nodes(current_node)
        end_time = time.time()
        elapsed_time = end_time - start_time
        if elapsed_time > 60:
            return [], []
    solution_file_data.append((current_node.get_swapped_token(),
                              current_node.get_swap_cost(), current_node.get_configuration()))
    solution_file_data.append((total_cost, elapsed_time))
    print(len(open_list))
    print(len(closed_list))
    
    return solution_file_data, search_file_data
