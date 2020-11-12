from dataExport import generate_solution_file, generate_search_file
from puzzle import Puzzle
import UCS
import GBFS
import A_star

# filename = 'samplePuzzles.txt'
# with open (filename) as file_object:
#     for line in file_object:
#         print(line)

puzzle = Puzzle([4,2,3,1,5,6,7,0,8], 3, 3)

# puzzle = Puzzle([1, 2, 3, 4, 0, 5, 6, 7], 4, 2)
# puzzle = Puzzle([3, 1, 0, 2], 2, 2)
# puzzle = Puzzle([0,8,3,7,6,1,5,2,4], 3, 3)

#solution_file_data, search_file_data = UCS.apply_algorithm(puzzle)
#print(solution_file_data)
#print(search_file_data)
#generate_solution_file(solution_file_data, 0, "ucs", "")
#generate_search_file(search_file_data, 0, "ucs", "")

# for i in solution_file_data:
#     print(i)
# for i in search_file_data:
#     print(i)

solution_file_data, search_file_data = GBFS.apply_algorithm(puzzle, 2) # 2nd argument is heuristic number
print(solution_file_data)
print(search_file_data)
#generate_solution_file(solution_file_data, 0, "GBFS", "-h1")
#generate_search_file(search_file_data, 0, "GBFS", "-h1")