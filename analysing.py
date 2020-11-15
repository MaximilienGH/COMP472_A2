class analysing():
    """A class to represent a puzzle node."""

    def __init__(self, total_number):
        self.total_number = total_number
        self.no_solution = 0
        self.cost = 0
        self.search_length = 0
        self.solution_length = 0
        self.exection_time = 0

    def add_search_length(self, search_length):
        self.search_length += search_length

    def add_solution_length(self, solution_length):
        self.solution_length += solution_length

    def add_time(self, time):
        self.exection_time += time

    def add_no_solution(self):
        self.no_solution += 1

    def add_cost(self, cost):
        self.cost += cost

    def get_cost(self):
        return self.cost

    def get_time(self):
        return self.exection_time

    def get_no_solution(self):
        return self.no_solution

    def get_search_length(self):
        return self.search_length

    def get_solution_length(self):
        return self.solution_length



