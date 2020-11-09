
class Puzzle():
    """A class to represent a puzzle."""
    
    def __init__(self):
        self.initial_state = [1, 2, 3, 4, 5, 6, 7, 0]
        self.current_state = self.initial_state 
        self.goal_state_1 = [1, 2, 3, 4, 5, 6, 7, 0]
        self.goal_state_2 = [1, 3, 5, 7, 2, 4, 6, 0]
        self.row_length = 4
        self.column_length = 2
        self.cost = 0
    
    # def is_tile_in_corner():
        
    
    # def is_swappable(index_of_tile_number):
        
    #     # If empty tile is not next to it, can't swap!
    #     if self.current_state[index_of_tile_number-1] != 0 and self.current_state[index_of_tile_number+1]:
    #         return False
    #     return True
    
    def locate_empty_tile(self):
        return self.current_state.index(0)
    
    def swap_tiles(self, empty_tile_index, tile_index):
        tile_number = self.current_state[tile_index]
        self.current_state[tile_index] = self.current_state[empty_tile_index]
        self.current_state[empty_tile_index] = tile_number
    
    def move_left(self):
        empty_tile_index = self.locate_empty_tile()
        distance = 1
        left_tile_index = empty_tile_index - distance
        self.swap_tiles(empty_tile_index, left_tile_index)
        self.cost += 1
        
    def move_right(self):
        empty_tile_index = self.locate_empty_tile()
        distance = 1
        right_tile_index = empty_tile_index + distance
        self.swap_tiles(empty_tile_index, right_tile_index)
        self.cost += 1
        
    def move_down(self):
        empty_tile_index = self.locate_empty_tile()
        distance = self.row_length
        lower_tile_index = empty_tile_index + distance
        self.swap_tiles(empty_tile_index, lower_tile_index)
        self.cost += 1
        
    def move_up(self):
        empty_tile_index = self.locate_empty_tile()
        distance = self.row_length
        upper_tile_index = empty_tile_index - distance
        self.swap_tiles(empty_tile_index, upper_tile_index)
        self.cost += 1
        
    def wrap_left(self):
        empty_tile_index = self.locate_empty_tile()
        distance = self.row_length - 1
        right_tile_index = empty_tile_index + distance
        self.swap_tiles(empty_tile_index, right_tile_index)
        self.cost += 2
        
    def wrap_right(self):
        empty_tile_index = self.locate_empty_tile()
        distance = self.row_length - 1
        left_tile_index = empty_tile_index - distance
        self.swap_tiles(empty_tile_index, left_tile_index)
        self.cost += 2
    
    def wrap_down(self):
        empty_tile_index = self.locate_empty_tile()
        distance = self.row_length * (self.column_length - 1)
        upper_tile_index = empty_tile_index - distance 
        self.swap_tiles(empty_tile_index, upper_tile_index)
        self.cost += 2
        
    def wrap_up(self):
        empty_tile_index = self.locate_empty_tile()
        distance = self.row_length * (self.column_length - 1)
        lower_tile_index = empty_tile_index + distance
        self.swap_tiles(empty_tile_index, lower_tile_index)
        self.cost += 2
    
    def move_diag_down_left(self):
        empty_tile_index = self.locate_empty_tile()
        distance = self.row_length - 1
        lower_left_tile_index = empty_tile_index + distance
        self.swap_tiles(empty_tile_index, lower_left_tile_index)
        self.cost += 3
        
    def move_diag_down_right(self):
        empty_tile_index = self.locate_empty_tile()
        distance = self.row_length + 1
        lower_right_tile_index = empty_tile_index + distance
        self.swap_tiles(empty_tile_index, lower_right_tile_index)
        self.cost += 3
    
    def move_diag_up_left(self):
        empty_tile_index = self.locate_empty_tile()
        distance = self.row_length + 1
        upper_left_tile_index = empty_tile_index - distance
        self.swap_tiles(empty_tile_index, upper_left_tile_index)
        self.cost += 3
        
    def move_diag_up_right(self):
        empty_tile_index = self.locate_empty_tile()
        distance = self.row_length - 1
        upper_right_tile_index = empty_tile_index - distance
        self.swap_tiles(empty_tile_index, upper_right_tile_index)
        self.cost += 3
        
    def wrap_diag_down_left(self):
        empty_tile_index = self.locate_empty_tile()
        distance = self.row_length * (self.column_length - 2) + 1
        upper_right_tile_index = empty_tile_index - distance
        self.swap_tiles(empty_tile_index, upper_right_tile_index)
        self.cost += 3
        
    def wrap_diag_down_right(self):
        empty_tile_index = self.locate_empty_tile()
        distance = self.row_length * self.column_length - 1
        upper_left_tile_index = empty_tile_index - distance
        self.swap_tiles(empty_tile_index, upper_left_tile_index)
        self.cost += 3
    
    def wrap_diag_up_left(self):
        empty_tile_index = self.locate_empty_tile()
        distance = self.row_length * self.column_length - 1
        lower_right_tile_index = empty_tile_index + distance
        self.swap_tiles(empty_tile_index, lower_right_tile_index)
        self.cost += 3
        
    def wrap_diag_up_right(self):
        empty_tile_index = self.locate_empty_tile()
        distance = self.row_length * (self.column_length - 2) + 1
        lower_left_tile_index = empty_tile_index + distance
        self.swap_tiles(empty_tile_index, lower_left_tile_index)
        self.cost += 3


puz = Puzzle()      
print(puz.current_state)
puz.wrap_diag_down_right()
puz.wrap_left()
puz.wrap_diag_up_right()
puz.wrap_diag_down_left()
print(puz.cost)
print(puz.current_state)