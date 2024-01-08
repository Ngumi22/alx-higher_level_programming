#!/usr/bin/python3

def print_matrix_integer(matrix=[[]]):
    for row in matrix:
        for col_index, value in enumerate(row):
            if col_index == len(row) - 1:
                print("{:d}".format(value), end="")
            else:
                print("{:d} ".format(value), end="")
        print()
