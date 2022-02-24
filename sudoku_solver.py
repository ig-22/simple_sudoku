import argparse


def input_reader(picture_path):
	"""
	This function takes the path of input picture.
	Then, it will return 2D matrix as python list.
	Example input picture can be found in directory.
	Example output:
	matrix = [
		[0,0,0,2,6,0,7,0,1],
		[6,8,0,0,7,0,0,9,0],
		[1,9,0,0,0,4,5,0,0],
		[8,2,0,1,0,0,0,4,0],
		[0,0,4,6,0,2,9,0,0],
		[0,5,0,0,0,3,0,2,8],
		[0,0,9,3,0,0,0,7,4],
		[0,4,0,0,5,0,0,3,6],
		[7,0,3,0,1,8,0,0,0]
	]
	"""
	return matrix


def pretty_print_sudoku_table(matrix):
	"""
	This function takes 2D matrix as python list.
	Then, prints it pretty.
	Example input:
	matrix = [
		[0,0,0,2,6,0,7,0,1],
		[6,8,0,0,7,0,0,9,0],
		[1,9,0,0,0,4,5,0,0],
		[8,2,0,1,0,0,0,4,0],
		[0,0,4,6,0,2,9,0,0],
		[0,5,0,0,0,3,0,2,8],
		[0,0,9,3,0,0,0,7,4],
		[0,4,0,0,5,0,0,3,6],
		[7,0,3,0,1,8,0,0,0]
	]
	Example print:
	7 8 0  |  4 0 0  |  1 2 0
	6 0 0  |  0 7 5  |  0 0 9
	0 0 0  |  6 0 1  |  0 7 8
	-------------------------
	0 0 7  |  0 4 0  |  2 6 0
	0 0 1  |  0 5 0  |  9 3 0
	9 0 4  |  0 6 0  |  0 0 5
	-------------------------
	0 7 0  |  3 0 0  |  0 1 2
	1 2 0  |  0 0 7  |  4 0 0
	0 4 9  |  2 0 6  |  0 0 7
	"""


def solver(matrix):
	"""
	This function takes sudoku input as 2D matrix with size of (9, 9).
	Empty areas represented as zeros.
	Hint: You can use numpy for selection from matrix.
	Example input:
	matrix = [
		[0,0,0,2,6,0,7,0,1],
		[6,8,0,0,7,0,0,9,0],
		[1,9,0,0,0,4,5,0,0],
		[8,2,0,1,0,0,0,4,0],
		[0,0,4,6,0,2,9,0,0],
		[0,5,0,0,0,3,0,2,8],
		[0,0,9,3,0,0,0,7,4],
		[0,4,0,0,5,0,0,3,6],
		[7,0,3,0,1,8,0,0,0]
	]
	Example output:
	matrix_solved = [
		[4,3,5,2,6,9,7,8,1],
		[6,8,2,5,7,1,4,9,3],
		[1,9,7,8,3,4,5,6,2],
		[8,2,6,1,9,5,3,4,7],
		[3,7,4,6,8,2,9,1,5],
		[9,5,1,7,4,3,6,2,8],
		[5,1,9,3,2,6,8,7,4],
		[2,4,8,9,5,7,1,3,6],
		[7,6,3,4,1,8,2,5,9]
	]
	"""
	return matrix_solved


if __name__ == "__main__":
	# Input path parser.
	parser = argparse.ArgumentParser()
	parser.add_argument('-path', type=str, default="sudoku_input.png", help="Path to sudoku input image.")
	args = parser.parse_args()
	file_path = args.path
	print(file_path)

	# Main code.
	matrix = input_reader(file_path)
	print("Sudoku input image is read!")
	print("This is the input sudoku problem.")
	pretty_print_sudoku_table(matrix)
	matrix_solved = solver(matrix)
	print("Sudoku is solved!")
