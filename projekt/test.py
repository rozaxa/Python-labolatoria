import pytest
import numpy as np

from projekt.main import kadane_for_1D
from projekt.main import kadane_for_2D


def test_kadane1D():
    matrix_1 = np.array([-2, 3, -1, 2])
    assert kadane_for_1D(matrix_1) == (4,1,3)

    matrix_2 = np.array([-2, -3, 4, -1, -2, 1, 5, -3])
    assert kadane_for_1D(matrix_2) == (7, 2, 6)

    matrix_3 = np.array([-3, -4, 5, -1, 2, -4, 6, -1])
    assert kadane_for_1D(matrix_3) == (8,2,6)

    matrix_4 = np.array([1, 2, 3, -5, 1, 1, -3, 0, 0, 1])
    assert kadane_for_1D(matrix_4) == (6, 0, 2)

    matrix_5 = np.array([-1, -2, -3, -6])
    assert kadane_for_1D(matrix_5) == (0, -1, -1)

    matrix_6 = np.array([1, 0, 0,-6])
    assert kadane_for_1D(matrix_6) == (1, 0, 0)

    matrix_7 = np.array([-2,-5,0,0,1,11,3,-2])
    assert kadane_for_1D(matrix_7) == (15, 4, 6)

    matrix_6 = np.array([0,0,0,0])
    assert kadane_for_1D(matrix_6) == (0, 0, 0)



def test_kadane2D():
    matrix_1 = np.array([[1,1,1], [2,2,2]])
    assert kadane_for_2D(matrix_1) == (9.0, [0, 0], [1, 2])

    matrix_2 = np.array([[1, 2, 3], [-2, 4, -3]])
    assert kadane_for_2D(matrix_2) == (6.0, [0, 0], [0, 2])

    matrix_3 = np.array([[-2,-3,1], [-3,-3,2]])
    assert kadane_for_2D(matrix_3) == (3.0, [0, 2], [1, 2])

    matrix_4 = np.array([[-4,-5,-6],[3,3,3]])
    assert kadane_for_2D(matrix_4) == (9.0, [1, 0], [1, 2])

    matrix_5 = np.array([[-4, -5, -6], [3, 3, 3], [3, 3, 3], [3, 3, 3], [3, 3, 3]])
    assert kadane_for_2D(matrix_5) == (36.0, [1, 0], [4, 2])

    matrix_6 = np.array([[-4, -5, -6], [-23, 3, 13], [1, -3, -7], [1, 2, 0], [0, -78, -2]])
    assert kadane_for_2D(matrix_6) == (16.0, [1, 1], [1, 2])

    matrix_7 = np.array([[-4, -5, -6], [-23, 3, 13], [1, -3, -7], [1, 2, 0], [0, -78, -2], [9, -1, 24], [0, 0, 0]])
    assert kadane_for_2D(matrix_7) == (32.0, [5, 0], [5, 2])

    matrix_8 = np.array([[8, 4, -4, 5], [9, 3, -7, 11], [1, 2, 6, 14], [-10, 8, 15, -1], [2, 11, 6, 4]])
    assert kadane_for_2D(matrix_8) == (87.0, [0, 0], [4, 3])

    matrix_9 = np.array([[-10, 8, 15, -1], [-10, 8, 15, -1], [1, 2, 6, 14], [-10, 8, 15, -1], [2, 11, 6, 4]])
    assert kadane_for_2D(matrix_9) == (109.0, [0, 1], [4, 3])

    matrix_10 = np.array([[-1, -2, -3], [-2, -5, -3]])
    assert kadane_for_2D(matrix_10) == (0, [-1, -1], [-1, -1])
























