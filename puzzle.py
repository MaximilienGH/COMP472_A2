
class Puzzle():
    """A class to represent a puzzle node."""
    
    def __init__(self, configuration, row_length, column_length): # Might include initial state + goal states or might remove them all together
        self.initial_state = configuration
        self.current_state = self.initial_state # might change
        self.goal_state_1 = [1, 2, 3, 4, 5, 6, 7, 8, 0] #[1, 2, 3, 4, 5, 6, 7, 8, 0] # [1, 2, 3, 0]  # [1, 2, 3, 4, 5, 6, 7, 0]
        self.goal_state_2 = [1, 4, 7, 2, 8, 5, 3, 6, 0] #[1, 4, 7, 2, 8, 5, 3, 6, 0] # [1, 2, 3, 0]  # [1, 3, 5, 7, 2, 4, 6, 0]
        self.ancestor_states = []
        self.row_length = row_length
        self.column_length = column_length
        self.g = 0 # Cost from root to node
        self.h = 0
        self.f = 0
        self.swapped_token = 0
        self.swap_cost = 0
    
    def get_g(self):
        """Returns the cost from root to current node."""
        return self.g
    
    def get_h(self):
        """Returns the estimated cost from node to goal node."""
        return self.h
    
    def get_f(self):
        """Returns the combined cost of g and h."""
        return self.f
    
    def get_configuration(self):
        """Returns the current configuration of the puzzle."""
        return self.current_state
    
    def get_swapped_token(self):
        """Returns the swapped token."""
        return self.swapped_token
    
    def get_swap_cost(self):
        """Returns the cost of the swap."""
        return self.swap_cost
    
    def get_ancestors(self):
        """Returns list of ancestor puzzle objects for a node."""
        return self.ancestor_states
    
    # def add_ancestor(self, parent_node):
    #     """Register parent node in order to track back to root node."""
    #     self.ancestor_states.append(parent_node)
    
    def is_goal(self):
        """Determines if current node is the goal or not."""
        return (self.current_state == self.goal_state_1) or (self.current_state == self.goal_state_2)
    
    def locate_empty_tile(self):
        """Determines the index of the empty tile in the puzzle."""
        return self.current_state.index(0)
        
    def swap_tiles(self, empty_tile_index, tile_index):
        """Swap the index of the empty tile with another one."""
        self.swapped_token = self.current_state[tile_index]
        self.current_state[tile_index] = self.current_state[empty_tile_index]
        self.current_state[empty_tile_index] = self.swapped_token
    
    def move_left(self, parent_node):
        empty_tile_index = self.locate_empty_tile()
        # If on left edge, can't move left
        if empty_tile_index in range(0, len(self.current_state), self.row_length):
            return
        distance = 1
        left_tile_index = empty_tile_index - distance
        self.swap_tiles(empty_tile_index, left_tile_index)
        self.swap_cost = 1
        self.g += self.swap_cost
        self.ancestor_states.append(parent_node)
        return self
        
    def move_right(self, parent_node):
        empty_tile_index = self.locate_empty_tile()
        # If on right edge, can't move right
        if empty_tile_index in range(self.row_length-1, len(self.current_state), self.row_length):
            return
        distance = 1
        right_tile_index = empty_tile_index + distance
        self.swap_tiles(empty_tile_index, right_tile_index)
        self.swap_cost = 1
        self.g += self.swap_cost
        self.ancestor_states.append(parent_node)
        return self
        
    def move_down(self, parent_node):
        empty_tile_index = self.locate_empty_tile()
        # If on bottom edge, can't move down
        if empty_tile_index in range(len(self.current_state)-self.row_length, len(self.current_state)):
            return
        distance = self.row_length
        lower_tile_index = empty_tile_index + distance
        self.swap_tiles(empty_tile_index, lower_tile_index)
        self.swap_cost = 1
        self.g += self.swap_cost
        self.ancestor_states.append(parent_node)
        return self
        
    def move_up(self, parent_node):
        empty_tile_index = self.locate_empty_tile()
        # If on top edge, can't move up
        if empty_tile_index in range(0, self.row_length):
            return
        distance = self.row_length
        upper_tile_index = empty_tile_index - distance
        self.swap_tiles(empty_tile_index, upper_tile_index)
        self.swap_cost = 1
        self.g += self.swap_cost
        self.ancestor_states.append(parent_node)
        return self
        
    def wrap_left(self, parent_node):
        empty_tile_index = self.locate_empty_tile()
        # If not in left corner, can't wrap left
        if empty_tile_index not in [0, len(self.current_state)-self.row_length]:
            return
        distance = self.row_length - 1
        right_tile_index = empty_tile_index + distance
        self.swap_tiles(empty_tile_index, right_tile_index)
        self.swap_cost = 2
        self.g += self.swap_cost
        self.ancestor_states.append(parent_node)
        return self
        
    def wrap_right(self, parent_node):
        empty_tile_index = self.locate_empty_tile()
        # If not in right corner, can't wrap right
        if empty_tile_index not in [self.row_length-1, len(self.current_state)-1]:
            return
        distance = self.row_length - 1
        left_tile_index = empty_tile_index - distance
        self.swap_tiles(empty_tile_index, left_tile_index)
        self.swap_cost = 2
        self.g += self.swap_cost
        self.ancestor_states.append(parent_node)
        return self
    
    def wrap_down(self, parent_node):
        empty_tile_index = self.locate_empty_tile()
        # If not in bottom corner, can't wrap down
        if empty_tile_index not in [len(self.current_state)-self.row_length, len(self.current_state)-1]:
            return
        distance = self.row_length * (self.column_length - 1)
        upper_tile_index = empty_tile_index - distance 
        self.swap_tiles(empty_tile_index, upper_tile_index)
        self.swap_cost = 2
        self.g += self.swap_cost
        self.ancestor_states.append(parent_node)
        return self
        
    def wrap_up(self, parent_node):
        empty_tile_index = self.locate_empty_tile()
        # If not in top corner, can't wrap up
        if empty_tile_index not in [0, self.row_length-1]:
            return
        distance = self.row_length * (self.column_length - 1)
        lower_tile_index = empty_tile_index + distance
        self.swap_tiles(empty_tile_index, lower_tile_index)
        self.swap_cost = 2
        self.g += self.swap_cost
        self.ancestor_states.append(parent_node)
        return self
    
    def move_diag_down_left(self, parent_node):
        empty_tile_index = self.locate_empty_tile()
        # If not in top right corner, can't move
        if empty_tile_index != self.row_length-1:
            return
        distance = self.row_length - 1
        lower_left_tile_index = empty_tile_index + distance
        self.swap_tiles(empty_tile_index, lower_left_tile_index)
        self.swap_cost = 3
        self.g += self.swap_cost
        self.ancestor_states.append(parent_node)
        return self
        
    def move_diag_down_right(self, parent_node):
        empty_tile_index = self.locate_empty_tile()
        # If not in top left corner, can't move
        if empty_tile_index != 0:
            return
        distance = self.row_length + 1
        lower_right_tile_index = empty_tile_index + distance
        self.swap_tiles(empty_tile_index, lower_right_tile_index)
        self.swap_cost = 3
        self.g += self.swap_cost
        self.ancestor_states.append(parent_node)
        return self
    
    def move_diag_up_left(self, parent_node):
        empty_tile_index = self.locate_empty_tile()
        # If not in bottom right corner, can't move
        if empty_tile_index != len(self.current_state)-1:
            return
        distance = self.row_length + 1
        upper_left_tile_index = empty_tile_index - distance
        self.swap_tiles(empty_tile_index, upper_left_tile_index)
        self.swap_cost = 3
        self.g += self.swap_cost
        self.ancestor_states.append(parent_node)
        return self
        
    def move_diag_up_right(self, parent_node):
        empty_tile_index = self.locate_empty_tile()
        # If not in bottom left corner, can't move
        if empty_tile_index != len(self.current_state)-self.row_length:
            return
        distance = self.row_length - 1
        upper_right_tile_index = empty_tile_index - distance
        self.swap_tiles(empty_tile_index, upper_right_tile_index)
        self.swap_cost = 3
        self.g += self.swap_cost
        self.ancestor_states.append(parent_node)
        return self
        
    def wrap_diag_down_left(self, parent_node):
        empty_tile_index = self.locate_empty_tile()
        # If not in bottom left corner, can't move
        if empty_tile_index != len(self.current_state)-self.row_length:
            return
        distance = self.row_length * (self.column_length - 2) + 1
        upper_right_tile_index = empty_tile_index - distance
        self.swap_tiles(empty_tile_index, upper_right_tile_index)
        self.swap_cost = 3
        self.g += self.swap_cost
        self.ancestor_states.append(parent_node)
        return self
        
    def wrap_diag_down_right(self, parent_node):
        empty_tile_index = self.locate_empty_tile()
        # If not in bottom right corner, can't move
        if empty_tile_index != len(self.current_state)-1:
            return
        distance = self.row_length * self.column_length - 1
        upper_left_tile_index = empty_tile_index - distance
        self.swap_tiles(empty_tile_index, upper_left_tile_index)
        self.swap_cost = 3
        self.g += self.swap_cost
        self.ancestor_states.append(parent_node)
        return self
    
    def wrap_diag_up_left(self, parent_node):
        empty_tile_index = self.locate_empty_tile()
        # If not in top left corner, can't move
        if empty_tile_index != 0:
            return
        distance = self.row_length * self.column_length - 1
        lower_right_tile_index = empty_tile_index + distance
        self.swap_tiles(empty_tile_index, lower_right_tile_index)
        self.swap_cost = 3
        self.g += self.swap_cost
        self.ancestor_states.append(parent_node)
        return self
        
    def wrap_diag_up_right(self, parent_node):
        empty_tile_index = self.locate_empty_tile()
        # If not in top right corner, can't move
        if empty_tile_index != self.row_length-1:
            return
        distance = self.row_length * (self.column_length - 2) + 1
        lower_left_tile_index = empty_tile_index + distance
        self.swap_tiles(empty_tile_index, lower_left_tile_index)
        self.swap_cost = 3
        self.g += self.swap_cost
        self.ancestor_states.append(parent_node)
        return self
    
    # Not 100% sure if that is what they want!
    def apply_heuristic_0(self):
        if (self.current_state[-1] == 0):
            self.h = 0
        else:
            self.h = 1
        
    def apply_heuristic_1(self):
        """Using Hamming distance to count number of tiles out of place."""
        temp_1 = 0
        temp_2 = 0
        for i in range(len(self.current_state)):
            if self.current_state[i] == 0:
                continue
            else:
                if self.current_state[i] != self.goal_state_1[i]:
                    temp_1 += 1
                if self.current_state[i] != self.goal_state_2[i]:
                    temp_2 += 1
        self.h = min(temp_1, temp_2)
        
    # Does not always give expected result!
    def apply_heuristic_2(self):
        """Using Manhattan distance to sum up all the distances bywhich tiles are out of place."""
        temp_1 = 0
        temp_2 = 0
        temp_1 = sum(abs(a%self.row_length - b%self.row_length)
                     + abs(a//self.column_length - b//self.column_length)
                         for a, b in ((self.current_state.index(i), self.goal_state_1.index(i))
                             for i in range(1, len(self.current_state))))
        temp_2 = sum(abs(a%self.row_length - b%self.row_length)
                     + abs(a//self.column_length - b//self.column_length)
                         for a, b in ((self.current_state.index(i), self.goal_state_2.index(i))
                             for i in range(1, len(self.current_state))))
        # print("h2 => g1=>", temp_1)
        # print("h2 => g2=>", temp_2)
        self.h = min(temp_1, temp_2)


# puz = Puzzle()      
# print(puz.current_state)
# # print(puz.h)
# # puz.apply_heuristic_2()
# # print(puz.h)
# for x in range(0, puz.row_length):
#     print(x)
# # for x in range(9-3, 9, ):
# #     print(x)


# puz.wrap_diag_down_right()
# puz.wrap_left()
# puz.wrap_diag_up_right()
# puz.wrap_diag_down_left()
# print(puz.g)
# print(puz.current_state)