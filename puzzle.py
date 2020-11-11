import copy
import sys
import time
class Puzzle_Node():
    """A class to represent a puzzle node."""

    def __init__(self):
        self.initial_state = [1, 7, 3, 4, 5, 6, 2, 0]
        self.current_state = self.initial_state
        self.goal_state_1 = [1, 2, 3, 4, 5, 6, 7, 0]
        self.goal_state_2 = [1, 3, 5, 7, 2, 4, 6, 0]
        self.row_length = 2
        self.column_length = 4
        self.cost = 0
        self.h = 0


    def locate_empty_tile(self):
        return self.current_state.index(0)

    def swap_tiles(self, empty_tile_index, tile_index):
        tile_number = self.current_state[tile_index]
        self.current_state[tile_index] = self.current_state[empty_tile_index]
        self.current_state[empty_tile_index] = tile_number

    def goal(self):
        if (self.current_state == self.goal_state_1) or (self.current_state == self.goal_state_2):
            return True
        else:
            return False

    def configuration(self):
        return self.current_state

    def move_left(self):
        empty_tile_index = self.locate_empty_tile()
        # If on left edge, can't move left
        if empty_tile_index in range(0, len(self.current_state), self.column_length):
            return
        distance = 1
        left_tile_index = empty_tile_index - distance
        self.swap_tiles(empty_tile_index, left_tile_index)
        self.cost += 1

    def move_right(self):
        empty_tile_index = self.locate_empty_tile()
        # If on right edge, can't move right
        if empty_tile_index in range(self.column_length - 1, len(self.current_state), self.column_length):
            return
        distance = 1
        right_tile_index = empty_tile_index + distance
        self.swap_tiles(empty_tile_index, right_tile_index)
        self.cost += 1

    def move_down(self):
        empty_tile_index = self.locate_empty_tile()
        # If on bottom edge, can't move down
        if empty_tile_index in range(len(self.current_state) - self.column_length_length, len(self.current_state)):
            return
        distance = self.column_length
        lower_tile_index = empty_tile_index + distance
        self.swap_tiles(empty_tile_index, lower_tile_index)
        self.cost += 1

    def move_up(self):
        empty_tile_index = self.locate_empty_tile()
        # If on top edge, can't move up
        if empty_tile_index in range(0, self.column_length):
            return
        distance = self.column_length
        upper_tile_index = empty_tile_index - distance
        self.swap_tiles(empty_tile_index, upper_tile_index)
        self.cost += 1
    '''
    def wrap_left(self):
        empty_tile_index = self.locate_empty_tile()
        # If not in left corner, can't wrap left
        if empty_tile_index not in [0, len(self.current_state) - self.column_length]:
            return
        distance = self.column_length - 1
        right_tile_index = empty_tile_index + distance
        self.swap_tiles(empty_tile_index, right_tile_index)

    def wrap_right(self):
        empty_tile_index = self.locate_empty_tile()
        # If not in right corner, can't wrap right
        if empty_tile_index not in [self.column_length - 1, len(self.current_state) - 1]:
            return
        distance = self.column_length - 1
        left_tile_index = empty_tile_index - distance
        self.swap_tiles(empty_tile_index, left_tile_index)
    '''
    def wrap(self):
        empty_tile_index = self.locate_empty_tile()
        top_left = 0
        top_right = self.column_length - 1
        bottom_left = len(self.current_state) - self.column_length
        bottom_right = len(self.current_state) - 1
        distance = 0
        if (empty_tile_index == top_left) or (empty_tile_index == bottom_left):
            distance = self.column_length - 1
            right_tile_index = empty_tile_index + distance
            self.swap_tiles(empty_tile_index, right_tile_index)
        elif (empty_tile_index == top_right) or (empty_tile_index == bottom_right):
            distance = self.column_length - 1
            left_tile_index = empty_tile_index - distance
            self.swap_tiles(empty_tile_index, left_tile_index)
        else:
            print('Error in the empty tile, please try again')
            sys.exit(0)
        self.cost += 2
    '''
    def move_diag_down_left(self):
        empty_tile_index = self.locate_empty_tile()
        # If not in top right corner, can't move
        if empty_tile_index != self.column_length - 1:
            return
        distance = self.column_length - 1
        lower_left_tile_index = empty_tile_index + distance
        self.swap_tiles(empty_tile_index, lower_left_tile_index)

    def move_diag_down_right(self):
        empty_tile_index = self.locate_empty_tile()
        # If not in top left corner, can't move
        if empty_tile_index != 0:
            return
        distance = self.column_length + 1
        lower_right_tile_index = empty_tile_index + distance
        self.swap_tiles(empty_tile_index, lower_right_tile_index)

    def move_diag_up_left(self):
        empty_tile_index = self.locate_empty_tile()
        # If not in bottom right corner, can't move
        if empty_tile_index != len(self.current_state) - 1:
            return
        distance = self.column_length + 1
        upper_left_tile_index = empty_tile_index - distance
        self.swap_tiles(empty_tile_index, upper_left_tile_index)

    def move_diag_up_right(self):
        empty_tile_index = self.locate_empty_tile()
        # If not in bottom left corner, can't move
        if empty_tile_index != len(self.current_state) - self.column_length:
            return
        distance = self.column_length - 1
        upper_right_tile_index = empty_tile_index - distance
        self.swap_tiles(empty_tile_index, upper_right_tile_index)

    def wrap_diag_down_left(self):
        empty_tile_index = self.locate_empty_tile()
        # If not in bottom left corner, can't move
        if empty_tile_index != len(self.current_state) - self.column_length:
            return
        distance = self.column_length * (self.row_length - 2) + 1
        upper_right_tile_index = empty_tile_index - distance
        self.swap_tiles(empty_tile_index, upper_right_tile_index)

    def wrap_diag_down_right(self):
        empty_tile_index = self.locate_empty_tile()
        # If not in bottom right corner, can't move
        if empty_tile_index != len(self.current_state) - 1:
            return
        distance = self.column_length * self.row_length - 1 #same as len()
        upper_left_tile_index = empty_tile_index - distance
        self.swap_tiles(empty_tile_index, upper_left_tile_index)

    def wrap_diag_up_left(self):
        empty_tile_index = self.locate_empty_tile()
        # If not in top left corner, can't move
        if empty_tile_index != 0:
            return
        distance = self.column_length * self.row_length - 1
        lower_right_tile_index = empty_tile_index + distance #same as len()
        self.swap_tiles(empty_tile_index, lower_right_tile_index)

    def wrap_diag_up_right(self):
        empty_tile_index = self.locate_empty_tile()
        # If not in top right corner, can't move
        if empty_tile_index != self.row_length - 1:
            return
        distance = self.column * (self.row_length - 2) + 1
        lower_left_tile_index = empty_tile_index + distance
        self.swap_tiles(empty_tile_index, lower_left_tile_index)
    '''

    def diag_adj(self):
        empty_tile_index = self.locate_empty_tile()
        top_left = 0
        top_right = self.column_length - 1
        bottom_left = len(self.current_state) - self.column_length
        bottom_right = len(self.current_state) - 1

        distance = 0
        if empty_tile_index == top_left:
            distance = self.column_length + 1
            lower_right_tile_index = empty_tile_index + distance
            self.swap_tiles(empty_tile_index, lower_right_tile_index)
        elif empty_tile_index == top_right:
            distance = self.column_length - 1
            lower_left_tile_index = empty_tile_index + distance
            self.swap_tiles(empty_tile_index, lower_left_tile_index)
        elif empty_tile_index == bottom_left:
            distance = self.column_length - 1
            upper_right_tile_index = empty_tile_index - distance
            self.swap_tiles(empty_tile_index, upper_right_tile_index)
        elif empty_tile_index == bottom_right:
            distance = self.column_length + 1
            upper_left_tile_index = empty_tile_index - distance
            self.swap_tiles(empty_tile_index, upper_left_tile_index)
        else:
            print('Error in the empty tile, please try again')
            sys.exit(0)
        self.cost += 3

    def diag_opposed(self):
        empty_tile_index = self.locate_empty_tile()
        top_left = 0
        top_right = self.column_length - 1
        bottom_left = len(self.current_state) - self.column_length
        bottom_right = len(self.current_state) - 1

        distance = 0
        if empty_tile_index == top_left:
            distance = self.column_length * self.row_length - 1
            lower_right_tile_index = empty_tile_index + distance  # same as len()
            self.swap_tiles(empty_tile_index, lower_right_tile_index)
        elif empty_tile_index == top_right:
            distance = self.column * (self.row_length - 2) + 1
            lower_left_tile_index = empty_tile_index + distance
            self.swap_tiles(empty_tile_index, lower_left_tile_index)
        elif empty_tile_index == bottom_left:
            distance = self.column_length * (self.row_length - 2) + 1
            upper_right_tile_index = empty_tile_index - distance
            self.swap_tiles(empty_tile_index, upper_right_tile_index)
        elif empty_tile_index == bottom_right:
            distance = self.column_length * self.row_length - 1  # same as len()
            upper_left_tile_index = empty_tile_index - distance
            self.swap_tiles(empty_tile_index, upper_left_tile_index)
        else:
            print('Error in the empty tile, please try again')
            sys.exit(0)
        self.cost += 3

    def possible_moves(self):
        moves = []
        index = self.locate_empty_tile()
        top_left = 0
        top_right = self.column_length - 1
        bottom_left = len(self.current_state) - self.column_length
        bottom_right = len(self.current_state) - 1

        if (top_left <= index <= top_right):
            moves.append(('regular-down', 1))

            if (index == top_left):
                moves.append(('regular-right', 1))
                moves.append(('wrap', 2))
                moves.append(('diag_adj',3))
                moves.append(('diag_opposed', 3))
            elif (index == top_right):
                moves.append(('regular-left', 1))
                moves.append(('wrap', 2))
                moves.append(('diag_adj', 3))
                moves.append(('diag_opposed', 3))
            else:
                moves.append(('regular-left', 1))
                moves.append(('regular-right', 1))
        elif (bottom_left <= index <= bottom_right):
            moves.append(('regular-up', 1))

            if (index == bottom_left):
                moves.append(('regular-right', 1))
                moves.append(('wrap', 2))
                moves.append(('diag_adj', 3))
                moves.append(('diag_opposed', 3))
            elif (index == bottom_right):
                moves.append(('regular-left', 1))
                moves.append(('wrap', 2))
                moves.append(('diag_adj', 3))
                moves.append(('diag_opposed', 3))
            else:
                moves.append(('regular-left', 1))
                moves.append(('regular-right', 1))
        else:
            moves.append(('regular-up', 1))
            moves.append(('regular-down', 1))
            if index in range(0, len(self.current_state), self.column_length):
                moves.append(('regular-right', 1))
            elif index in range(self.column_length - 1, len(self.current_state), self.column_length):
                moves.append(('regular-left', 1))
            else:
                moves.append(('regular-left', 1))
                moves.append(('regular-right', 1))
        return moves



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
        temp_1 = sum(abs(a % self.row_length - b % self.row_length)
                     + abs(a // self.column_length - b // self.column_length)
                     for a, b in ((self.current_state.index(i), self.goal_state_1.index(i))
                                  for i in range(1, len(self.current_state))))
        temp_2 = sum(abs(a % self.row_length - b % self.row_length)
                     + abs(a // self.column_length - b // self.column_length)
                     for a, b in ((self.current_state.index(i), self.goal_state_2.index(i))
                                  for i in range(1, len(self.current_state))))
        # print("h2 => g1=>", temp_1)
        # print("h2 => g2=>", temp_2)
        self.h = min(temp_1, temp_2)

