# create a class UCS with attributes (maybe later)

open_list = []
closed_list = []
search_Path = []

def search_node():
    return

def find_children_nodes(current_node):
    global open_list
    open_list.append(current_node.move_left())
    open_list.append(current_node.move_right())
    open_list.append(current_node.move_down())
    open_list.append(current_node.move_up())
    open_list.append(current_node.wrap_left())
    open_list.append(current_node.wrap_right())
    open_list.append(current_node.wrap_down())
    open_list.append(current_node.wrap_up())
    open_list.append(current_node.move_diag_down_left())
    open_list.append(current_node.move_diag_down_right())
    open_list.append(current_node.move_diag_up_left())
    open_list.append(current_node.move_diag_up_right())
    open_list.append(current_node.wrap_diag_down_left())
    open_list.append(current_node.wrap_diag_down_right())
    open_list.append(current_node.wrap_diag_up_left())
    open_list.append(current_node.wrap_diag_up_right())
    
    open_list = filter(None, open_list)
    # sort open list

def apply_algorithm(start_node):
    global open_list, closed_list
    open_list.append(start_node)
    while(open_list):
        current_node = open_list.pop(0)
        closed_list.append(current_node)
        if current_node.configuration.is_goal():
            break
        find_children_nodes(current_node)

