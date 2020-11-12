
def flatten_list(non_flat_list):
    flat_list = [i for i in non_flat_list if not isinstance(i, list)]
    if isinstance(non_flat_list[-1], list):
        for j in non_flat_list[-1]:
            flat_list.append(j)
    return flat_list 

def generate_solution_file(solution_file_data, number, algorithm, heuristic):
    output_file = f"{number}_{algorithm}{heuristic}_solution.txt"
    with open(output_file, 'w') as file_object:
        if solution_file_data == None:
            file_object.write("no solution")
        else:
            for i in solution_file_data:
                flat_list = flatten_list(i)
                file_object.write(" ".join(list(map(str, flat_list))))
                file_object.write('\n')
        
def generate_search_file(search_file_data, number, algorithm, heuristic):
    output_file = f"{number}_{algorithm}{heuristic}_search.txt"
    with open(output_file, 'w') as file_object:
        if search_file_data == None:
            file_object.write("no solution")
        else:
            for i in search_file_data:
                flat_list = flatten_list(i)
                file_object.write(" ".join(list(map(str, flat_list))))
                file_object.write('\n')
                