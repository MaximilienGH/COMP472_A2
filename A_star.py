import copy
import time

# create a class GBFS with attributes (maybe later)

open_list = []
closed_list = []
cL = []
search_Path = []
solution_file_data = []
search_file_data = []

#def search_node():
#    return


def update_solution_file_data(goal_node):
    global solution_file_data
    for i in goal_node.get_ancestors():
        solution_file_data.append((i.get_swapped_token(),
                                   i.get_swap_cost(),
                                   i.get_configuration()))


def update_search_file_data(current_node):
    global search_file_data
    search_file_data.append((current_node.get_g() + current_node.get_h(),
                             current_node.get_g(),
                             current_node.get_h(),
                             current_node.get_configuration()))


def choose_heuristic(heuristic_number):
    if heuristic_number == 1:
        [i.apply_heuristic_1() for i in open_list]
    elif heuristic_number == 2:
        [i.apply_heuristic_2() for i in open_list]
    else:
        [i.apply_heuristic_0() for i in open_list]

    # print([i.get_h() for i in open_list])


def find_children_nodes(node, heuristic_number):
    global open_list,cL
    # print(node.get_configuration())
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
    # print(node.get_configuration())

    open_list = list(filter(None, open_list))
    choose_heuristic(heuristic_number)
    '''
        Get rid of all the duplicate configuration with larger cost
        As we are using the same h(n) for all the configurations
        there is no need for us to sort on h(n)
    '''
    open_list.sort(key=lambda x: (x.get_g()))
    temp_configuration = []
    temp_list = []

    for i in range(len(open_list)):
        if (open_list[i].get_configuration() not in temp_configuration) and (open_list[i].get_configuration() not in cL):
            temp_configuration.append(open_list[i].get_configuration())
            temp_list.append(open_list[i])


    open_list = temp_list
    open_list.sort(key=lambda x: (x.get_g()+x.get_h()))
    print('start point')
    for i in range(len(open_list)):
        print(open_list[i].get_configuration(),
              (open_list[i].get_h())+open_list[i].get_g())
    print("break point")
    print(cL)



# Must check if state is already in closed list and open list!
def apply_algorithm(start_node, heuristic_number):
    global open_list, closed_list, cL
    start_time = time.time()
    if heuristic_number == 1:
        start_node.apply_heuristic_1()
    elif heuristic_number == 2:
        start_node.apply_heuristic_2()
    else:
        start_node.apply_heuristic_0()
    open_list.append(start_node)
    total_cost = 0
    elapsed_time = 0
    while (open_list):
        current_node = open_list.pop(0)

        closed_list.append(current_node)
        cL.append(current_node.get_configuration())

        update_search_file_data(current_node)
        if current_node.is_goal():
            total_cost = current_node.get_g()
            update_solution_file_data(current_node)
            break

        find_children_nodes(current_node, heuristic_number)
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