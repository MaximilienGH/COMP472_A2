from puzzle import Puzzle
import UCS

# filename = 'samplePuzzles.txt'
# with open (filename) as file_object:
#     for line in file_object:
#         print(line)

puzzle = Puzzle([2, 0, 3, 4, 1, 5, 6, 7], 4, 2)
# puzzle = Puzzle([1, 2, 3, 4, 0, 5, 6, 7], 4, 2)
# puzzle = Puzzle([3, 1, 0, 2], 2, 2)
# puzzle = Puzzle([0,8,3,7,6,1,5,2,4], 3, 3)

solution_file_data, search_file_data = UCS.apply_algorithm(puzzle)

# for i in solution_file_data:
#     print(i)
for i in search_file_data:
    print(i)
