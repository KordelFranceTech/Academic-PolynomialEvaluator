# constants.py
# Kordel France
########################################################################################################################
# This file contains the specification for which single-character strings are allowed for the interpretation of the
# prefix strings in this program.
########################################################################################################################

#characters that are acceptable as operands for the evaluation of prefix strings.
acceptable_chars = ['A', 'B', 'C' ,'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z',
                    'a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z',
                    '*', '/', '+', '-', '0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
#characters that are acceptable as operators for the evaluation of prefix strings.
acceptable_operators = ['*', '+', '-']
acceptable_operands = ['A', 'B', 'C' ,'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z',
                        'a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']
acceptable_coeffs = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
acceptable_degs = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
operations_list = ['A + B', 'A + C', 'A + D', 'B + C', 'B + D', 'C + D', 'B - A', 'B - D', 'A * B', 'A * C', 'A * D',
                   'B * A', 'B * C', 'B * D', 'C * D']
eval_points = [[0, 1, 2], [1, 2, 3], [2, 1, 0], [4, -1, -4]]

