import copy
# create a class UCS with attributes (maybe later)

open_list = []
closed_list = []
search_Path = []
solution_file_data = []
search_file_data = []

def search_node():
    return

def find_children_nodes(node):
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
    open_list.sort(key=lambda x: x.get_g())

# Must check if state is already in closed list and open list!
def apply_algorithm(start_node):
    global open_list, closed_list
    open_list.append(start_node)
    while(open_list):
        current_node = open_list.pop(0)
        closed_list.append(current_node)
        print(current_node.get_configuration())
        if current_node.is_goal():
            break
        # current_node_copy = copy.deepcopy(current_node)
        find_children_nodes(current_node)
    print(len(open_list))
    print(len(closed_list))

