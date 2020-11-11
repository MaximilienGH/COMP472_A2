from puzzle import Puzzle
import UCS

# filename = 'samplePuzzles.txt'
# with open (filename) as file_object:
#     for line in file_object:
#         print(line)

puzzle = Puzzle([2, 0, 3, 4, 1, 5, 6, 7], 4, 2)
# puzzle = Puzzle([3, 1, 0, 2], 2, 2)
# puzzle = Puzzle([0,8,3,7,6,1,5,2,4], 3, 3)

UCS.apply_algorithm(puzzle)
