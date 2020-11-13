"""
File name:     data_Export.py
Authors:       Maximilien Fathi, Zihan Zhou
Date:          November 16, 2020
Description:   Code used for the creation of solution files and search files.
"""

def flatten_list(non_flat_list):
    """Flattens a list of lists and integers into a 1D list."""
    flat_list = [i for i in non_flat_list if not isinstance(i, list)]
    if isinstance(non_flat_list[-1], list):
        for j in non_flat_list[-1]:
            flat_list.append(j)
    return flat_list 

def generate_solution_file(solution_file_data, number, algorithm, heuristic):
    """Generates a file containing the solution found by the algorithm."""
    output_file = f"Output_Files/{number}_{algorithm}{heuristic}_solution.txt"
    with open(output_file, 'w') as file_object:
        if not solution_file_data:
            file_object.write("no solution")
        else:
            for i in solution_file_data:
                flat_list = flatten_list(i)
                file_object.write(" ".join(list(map(str, flat_list))))
                file_object.write('\n')
        
def generate_search_file(search_file_data, number, algorithm, heuristic):
    """Generates a file containing the search path used by the algorithm."""
    output_file = f"Output_Files/{number}_{algorithm}{heuristic}_search.txt"
    with open(output_file, 'w') as file_object:
        if not search_file_data:
            file_object.write("no solution")
        else:
            for i in search_file_data:
                flat_list = flatten_list(i)
                file_object.write(" ".join(list(map(str, flat_list))))
                file_object.write('\n')
                