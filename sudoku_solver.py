import argparse
import numpy as np
import matplotlib.pyplot as plt
import cv2
from PIL import Image
from tensorflow.keras.models import load_model
import tensorflow as tf
from skimage.transform import resize


def split_cells(img):
    rows = np.vsplit(img, 9)
    boxes = []
    for r in rows:
        cols = np.hsplit(r, 9)
        for box in cols:
            boxes.append(box)
    return boxes


def crop_cell(cells):
    cells_cropped = []
    for image in cells:
        img = np.array(image)
        img = img[4:46, 6:46]
        img = Image.fromarray(img)
        cells_cropped.append(img)
    return cells_cropped


def input_reader(picture_path):
    img = cv2.imread(picture_path)
    sudoku_a = cv2.resize(img, (450, 450))
    gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    blur = cv2.GaussianBlur(gray, (3, 3), 6)
    blur = cv2.bilateralFilter(gray, 9, 75, 75)
    threshold = cv2.adaptiveThreshold(blur, 255, 1, 1, 11, 2)
    plt.figure()
    plt.imshow(threshold)
    plt.show()

    contour_1 = sudoku_a.copy()
    contour_2 = sudoku_a.copy()
    contour, hierarchy = cv2.findContours(threshold, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)
    cv2.drawContours(contour_1, contour, -1, (0, 255, 0), 3)
    sudoku_cell = split_cells(threshold)

    sudoku_cell_cropped = crop_cell(sudoku_cell)

    model = tf.keras.models.load_model('model-OCR.h5')
    model.compile(optimizer='adam', loss='sparse_categorical_crossentropy', metrics=['accuracy'])

    predicted_numbers = []
    length_of_sudoku = range(len(sudoku_cell_cropped))

    for i in length_of_sudoku:
        foto = np.invert(np.array(sudoku_cell_cropped[i]))
        foto = resize(foto, (48, 48, 1))
        prediction = model.predict(foto.reshape(1, 48, 48, 1))
        index = np.argmax(prediction)
        if index == 0:
            predicted_numbers.append(0)
        elif index == 1:
            predicted_numbers.append(1)
        elif index == 2:
            predicted_numbers.append(2)
        elif index == 3:
            predicted_numbers.append(3)
        elif index == 4:
            predicted_numbers.append(4)
        elif index == 5:
            predicted_numbers.append(5)
        elif index == 6:
            predicted_numbers.append(6)
        elif index == 7:
            predicted_numbers.append(7)
        elif index == 8:
            predicted_numbers.append(8)
        elif index == 9:
            predicted_numbers.append(9)

    matrix = np.array(predicted_numbers).astype('uint8').reshape(9, 9)
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
    counter = 0
    for sublist in matrix:
        counter += 1
        if counter in range(1, 4):
            print(f'{sublist[:3]}  |  {sublist[3:6]}  |  {sublist[6:9]}')
        elif counter == 4:
            print('-------------------------------------')
            print(f'{sublist[:3]}  |  {sublist[3:6]}  |  {sublist[6:9]}')
        elif counter in range(5, 7):
            print(f'{sublist[:3]}  |  {sublist[3:6]}  |  {sublist[6:9]}')
        elif counter == 7:
            print('-------------------------------------')
            print(f'{sublist[:3]}  |  {sublist[3:6]}  |  {sublist[6:9]}')
        else:
            print(f'{sublist[:3]}  |  {sublist[3:6]}  |  {sublist[6:9]}')


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
    matrix_solved = matrix
    return matrix_solved


if __name__ == "__main__":
    # Input path parser.
    parser = argparse.ArgumentParser()
    parser.add_argument('-p', '--path', type=str, default="mysudoku.jpg", help="Path to sudoku input image.")
    args = parser.parse_args()
    file_path = args.path
    print(file_path)

    # Main code.
    matrix = input_reader(file_path)
    print("Sudoku input image is read!")
    print("This is the input sudoku problem.")
    pretty_print_sudoku_table(matrix)
    print('                                                 ')
    matrix_solved = solver(matrix)
    pretty_print_sudoku_table(matrix)
    print("Sudoku is solved!")
