import numpy as np

def kadane_for_1D(matrix):

    s = len(matrix)

    if s == 0:
        raise Exception("Size of the matrix = 0! Try again!")

    sum_max = 0
    sum_current = 0

    start_index = 0
    end_index = 0
    current_start = 0

    for index in range(0, s):

        sum_current = sum_current + matrix[index]

        if sum_current > sum_max:
            sum_max = sum_current
            end_index = index
            start_index = current_start

        if sum_current <= 0:
            sum_current = 0
            current_start = index + 1

    if matrix[0] < 0 and sum_max == 0 and start_index == 0:
        return 0, -1, -1

    return sum_max, start_index, end_index



def kadane_for_2D(matrix):
    max_sub_value = 0
    max_sub_start = [0,0]
    max_sub_end = [0,0]


    row = matrix.shape[0]
    col = matrix.shape[1]



    for left in range(col):

        sub = np.zeros(shape=row)


        for right in range(left, col):
            sub = sub + matrix[:, right]


            value_current, start_current, end_current = kadane_for_1D(sub)

            if value_current > max_sub_value:
                max_sub_value = value_current
                max_sub_start = [start_current, left]
                max_sub_end = [end_current, right]

    if matrix[0][0] < 0 and max_sub_value == 0 and max_sub_start == [0, 0]:
        return 0, [-1, -1], [-1, -1]

    return max_sub_value, max_sub_start, max_sub_end



