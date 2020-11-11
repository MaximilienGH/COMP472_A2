import puzzle
import UCS

# filename = 'samplePuzzles.txt'
# with open (filename) as file_object:
#     for line in file_object:
#         print(line)

puzzle = puzzle([1, 2, 3, 4, 5, 6, 0, 7], 4, 2)
UCS.apply_algorithm(puzzle)
