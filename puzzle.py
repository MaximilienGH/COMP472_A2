"""
File name:     puzzle.py
Authors:       Maximilien Fathi, Zihan Zhou
Date:          November 16, 2020
Description:   Code used for the creation of a Puzzle class.
"""
import math
import copy

class Puzzle():
    """A class to represent a puzzle node."""

    def __init__(self, initial_state, goal_state_1, goal_state_2, row_length, column_length):
        """A constructor to initialize the attributes of a Puzzle object."""
        self.initial_state = initial_state
        self.current_state = self.initial_state
        self.goal_state_1 = goal_state_1
        self.goal_state_2 = goal_state_2
        self.ancestor_states = []
        self.row_length = row_length
        self.column_length = column_length
        self.g = 0
        self.h = 0
        self.f = 0
        self.swapped_token = 0
        self.swap_cost = 0
    
    # Needed for UCS_WITH_PQ.py
    # def __lt__(self, other):
    #     return self.g < other.g
    def get_g(self):
        """Returns the cost from root to current node."""
        return self.g

    def get_h(self):
        """Returns the estimated lowest cost from node to goal node."""
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

    def __lt__(self, other):
        return self.get_g() < other.get_g()

    def get_ancestors(self):
        """Returns list of ancestor puzzle objects for a node."""
        return self.ancestor_states

    def determine_f(self):
        """Finds the combined cost of g and h."""
        self.f = self.g + self.h

    def is_goal(self):
        """Determines if current node is the goal or not."""
        return (self.current_state == self.goal_state_1) or (self.current_state == self.goal_state_2)

    def getgoal1(self):
        return self.goal_state_1

    def getgoal2(self):
        return self.goal_state_2

    def locate_empty_tile(self):
        """Determines the index of the empty tile in the puzzle."""
        return self.current_state.index(0)

    def swap_tiles(self, empty_tile_index, tile_index):
        """Swap the index of the empty tile with another one."""
        self.swapped_token = self.current_state[tile_index]
        self.current_state[tile_index] = self.current_state[empty_tile_index]
        self.current_state[empty_tile_index] = self.swapped_token

    def move_left(self, parent_node):
        """Regularly move the empty tile to the left."""
        empty_tile_index = self.locate_empty_tile()
        # If on left edge, can't move left
        if empty_tile_index in range(0, len(self.current_state), self.row_length):
            return None
        distance = 1
        left_tile_index = empty_tile_index - distance
        self.swap_tiles(empty_tile_index, left_tile_index)
        self.swap_cost = 1
        self.g += self.swap_cost
        self.ancestor_states.append((self.swapped_token, self.swap_cost, parent_node))
        return self

    def move_right(self, parent_node):
        """Regularly move the empty tile to the right."""
        empty_tile_index = self.locate_empty_tile()
        # If on right edge, can't move right
        if empty_tile_index in range(self.row_length - 1, len(self.current_state), self.row_length):
            return None
        distance = 1
        right_tile_index = empty_tile_index + distance
        self.swap_tiles(empty_tile_index, right_tile_index)
        self.swap_cost = 1
        self.g += self.swap_cost
        self.ancestor_states.append((self.swapped_token, self.swap_cost, parent_node))
        return self

    def move_down(self, parent_node):
        """Regularly move the empty tile down."""
        empty_tile_index = self.locate_empty_tile()
        # If on bottom edge, can't move down
        if empty_tile_index in range(len(self.current_state) - self.row_length, len(self.current_state)):
            return None
        distance = self.row_length
        lower_tile_index = empty_tile_index + distance
        self.swap_tiles(empty_tile_index, lower_tile_index)
        self.swap_cost = 1
        self.g += self.swap_cost
        self.ancestor_states.append((self.swapped_token, self.swap_cost, parent_node))
        return self

    def move_up(self, parent_node):
        """Regularly move the empty tile up."""
        empty_tile_index = self.locate_empty_tile()
        # If on top edge, can't move up
        if empty_tile_index in range(0, self.row_length):
            return None
        distance = self.row_length
        upper_tile_index = empty_tile_index - distance
        self.swap_tiles(empty_tile_index, upper_tile_index)
        self.swap_cost = 1
        self.g += self.swap_cost
        self.ancestor_states.append((self.swapped_token, self.swap_cost, parent_node))
        return self

    def wrap_horizontal(self, parent_node):
        empty_tile_index = self.locate_empty_tile()
        if empty_tile_index in [0, len(self.current_state) - self.row_length]:
            distance = self.row_length - 1
            right_tile_index = empty_tile_index + distance
            self.swap_tiles(empty_tile_index, right_tile_index)
            self.swap_cost = 2
            self.g += self.swap_cost
            self.ancestor_states.append((self.swapped_token, self.swap_cost, parent_node))
            return self
        elif empty_tile_index in [self.row_length - 1, len(self.current_state) - 1]:
            distance = self.row_length - 1
            left_tile_index = empty_tile_index - distance
            self.swap_tiles(empty_tile_index, left_tile_index)
            self.swap_cost = 2
            self.g += self.swap_cost
            self.ancestor_states.append((self.swapped_token, self.swap_cost, parent_node))
            return self
        else:
            return None

    def wrap_vertical(self,parent_node):
        empty_tile_index = self.locate_empty_tile()
        if empty_tile_index in [len(self.current_state) - self.row_length, len(self.current_state) - 1]:
            distance = self.row_length * (self.column_length - 1)
            upper_tile_index = empty_tile_index - distance
            self.swap_tiles(empty_tile_index, upper_tile_index)
            self.swap_cost = 2
            self.g += self.swap_cost
            self.ancestor_states.append((self.swapped_token, self.swap_cost, parent_node))
            return self
        elif empty_tile_index in [0, self.row_length - 1]:
            distance = self.row_length * (self.column_length - 1)
            lower_tile_index = empty_tile_index + distance
            self.swap_tiles(empty_tile_index, lower_tile_index)
            self.swap_cost = 2
            self.g += self.swap_cost
            self.ancestor_states.append((self.swapped_token, self.swap_cost, parent_node))
            return self
        else:
            return None

    def move_diag(self,parent_node):
        empty_tile_index = self.locate_empty_tile()
        if empty_tile_index == self.row_length - 1:
            distance = self.row_length - 1
            lower_left_tile_index = empty_tile_index + distance
            self.swap_tiles(empty_tile_index, lower_left_tile_index)
            self.swap_cost = 3
            self.g += self.swap_cost
            self.ancestor_states.append((self.swapped_token, self.swap_cost, parent_node))
            return self
        elif empty_tile_index == 0:
            distance = self.row_length + 1
            lower_right_tile_index = empty_tile_index + distance
            self.swap_tiles(empty_tile_index, lower_right_tile_index)
            self.swap_cost = 3
            self.g += self.swap_cost
            self.ancestor_states.append((self.swapped_token, self.swap_cost, parent_node))
            return self
        elif empty_tile_index == len(self.current_state) - 1:
            distance = self.row_length + 1
            upper_left_tile_index = empty_tile_index - distance
            self.swap_tiles(empty_tile_index, upper_left_tile_index)
            self.swap_cost = 3
            self.g += self.swap_cost
            self.ancestor_states.append((self.swapped_token, self.swap_cost, parent_node))
            return self
        elif empty_tile_index == len(self.current_state) - self.row_length:
            distance = self.row_length - 1
            upper_right_tile_index = empty_tile_index - distance
            self.swap_tiles(empty_tile_index, upper_right_tile_index)
            self.swap_cost = 3
            self.g += self.swap_cost
            self.ancestor_states.append((self.swapped_token, self.swap_cost, parent_node))
            return self
        else:
            return None

    def wrap_diag(self,parent_node):
        empty_tile_index = self.locate_empty_tile()
        if empty_tile_index == len(self.current_state) - self.row_length:
            distance = self.row_length * (self.column_length - 2) + 1
            upper_right_tile_index = empty_tile_index - distance
            self.swap_tiles(empty_tile_index, upper_right_tile_index)
            self.swap_cost = 3
            self.g += self.swap_cost
            self.ancestor_states.append((self.swapped_token, self.swap_cost, parent_node))
            return self
        elif empty_tile_index == len(self.current_state) - 1:
            distance = self.row_length * self.column_length - 1
            upper_left_tile_index = empty_tile_index - distance
            self.swap_tiles(empty_tile_index, upper_left_tile_index)
            self.swap_cost = 3
            self.g += self.swap_cost
            self.ancestor_states.append((self.swapped_token, self.swap_cost, parent_node))
            return self
        elif empty_tile_index == 0:
            distance = self.row_length * self.column_length - 1
            lower_right_tile_index = empty_tile_index + distance
            self.swap_tiles(empty_tile_index, lower_right_tile_index)
            self.swap_cost = 3
            self.g += self.swap_cost
            self.ancestor_states.append((self.swapped_token, self.swap_cost, parent_node))
            return self
        elif empty_tile_index == self.row_length - 1:
            distance = self.row_length * (self.column_length - 2) + 1
            lower_left_tile_index = empty_tile_index + distance
            self.swap_tiles(empty_tile_index, lower_left_tile_index)
            self.swap_cost = 3
            self.g += self.swap_cost
            self.ancestor_states.append((self.swapped_token, self.swap_cost, parent_node))
            return self
        else:
            return


    def apply_heuristic_0(self):
        """Applies a naive heuristic."""
        if self.current_state[-1] == 0:
            self.h = 0
        else:
            self.h = 1

    def apply_heuristic_1(self):
        """Applies a heuristic based on Hamming distance to count number of 
        tiles out of place."""
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


    '''
        temp_1 = 0
        temp_2 = 0
        for i in self.current_state:
            if i == 0:
                continue
            else:
                index = self.current_state.index(i)
                index_goal1 = self.goal_state_1.index(i)
                index_goal2 = self.goal_state_2.index(i)
                if index % self.row_length - index_goal1 % self.row_length != 0:
                    temp_1 += 1
                if index // self.column_length - index_goal1 // self.column_length != 0:
                    temp_1 += 1
                if index % self.row_length - index_goal2 % self.row_length != 0:
                    temp_2 += 1
                if index // self.column_length - index_goal2 // self.column_length != 0:
                    temp_2 += 1

        self.h = min(temp_1, temp_2)
    '''

    def apply_heuristic_2(self):
        """Applies a heuristic based on Manhattan distance to sum up 
        all the distances by which tiles are out of place."""

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
        self.h = min(temp_1, temp_2)

        '''
        #Euclidean Distance
        temp_1 = 0
        temp_2 = 0
        temp_1 = (sum(math.sqrt((a % self.row_length - b % self.row_length)*(a % self.row_length - b % self.row_length)
                    + (a // self.column_length - b // self.column_length) * (a // self.column_length - b // self.column_length))
                        for a, b in ((self.current_state.index(i), self.goal_state_1.index(i))
                            for i in range(1, len(self.current_state))))
                + sum(abs(a % self.row_length - b % self.row_length)
                     + abs(a // self.column_length - b // self.column_length)
                     for a, b in ((self.current_state.index(i), self.goal_state_1.index(i))
                                  for i in range(1, len(self.current_state))))) / 2
        temp_2 = (sum(math.sqrt((a % self.row_length - b % self.row_length)*(a % self.row_length - b % self.row_length)
                    + (a // self.column_length - b // self.column_length) * (a // self.column_length - b // self.column_length))
                        for a, b in ((self.current_state.index(i), self.goal_state_2.index(i))
                            for i in range(1, len(self.current_state))))
                  + sum(abs(a % self.row_length - b % self.row_length)
                     + abs(a // self.column_length - b // self.column_length)
                     for a, b in ((self.current_state.index(i), self.goal_state_2.index(i))
                                  for i in range(1, len(self.current_state))))) / 2
        self.h = min(temp_1, temp_2)
        '''
        '''
        temp_1 = 0
        temp_2 = 0
        state1 = copy.deepcopy(self.current_state)
        state2 = copy.deepcopy(self.current_state)

        for i in range(len(self.current_state)):
            index = state1.index(i)
            index_1 = self.goal_state_1.index(i)
            if index != index_1:
                temp = state1[index_1]
                state1[index_1] = i
                state1[index] = temp
                temp_1 += 1

            index = state2.index(i)
            index_2 = self.goal_state_2.index(i)

            if index != index_2:
                temp = state2[index_2]
                state2[index_2] = i
                state2[index] = temp
                temp_2 += 1

        self.h = min(temp_1, temp_2)
        '''

