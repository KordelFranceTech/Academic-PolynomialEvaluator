# file_processing.py
# Kordel France
########################################################################################################################
# This file contains functions that perform I/O file processing of the user-specified input and output files.
########################################################################################################################

from Lab3.CSLList import CSLList
from Lab3.Node import Node
from Lab3.CSLListOfCSLLists import CSLListOfCSLLists
from Lab3 import constants
import time


def process_file_data(input_text_file, output_text_file) -> None:
    """
    Takes an input file to read data from line by line, character by character, and cleans it for distribution into a
        a circular singly-linked list that represents polynomial expressions. We don't want to input garbage data into
        our linked list for evaluation, so data is first cleaned and then input into the CSL List.
    :param input_text_file: the text file to read polynomial data from.
    :param output_text_file: the text file to write evaluated polynomial expressions to.
    ;returns readin_array: the cleaned data file used for building the circularly linked lists of polynomials.
    ;returns output_text_file: the text file to write evaluated polynomial expressions to.
    """
    print('Processing input...')
    input_file = open(str(input_text_file), 'r')
    readin_array = []
    last_char = ''
    # read the entire file again into an array so it can be cleaned
    # clean the data as it is read
    while 1:
        single_char = input_file.read(1)
        if not single_char:
            break
        elif str(single_char) == ' ':
            continue
        elif single_char == '\n':
            if last_char == '\n':
                continue
            else:
                readin_array.append('\n')
        elif str(single_char) == '#':
            # '#' will be used later on as a delimiter for expression conversion
            # if the user put a '#' in their input file, replace it with a '@'
            readin_array.append('@')
        else:
            if str(single_char) in constants.acceptable_chars:
                readin_array.append(str(single_char))
        last_char = single_char
    input_file.close()
    return readin_array, output_text_file

def buildCircularSinglyLinkedLists(data, output_text_file):
    """
    Takes the cleaned input file and builds the circular singly linked list for each available polynomial term.
    Builds a linked list of these circular singly linked lists to represent a polynomial sequence.
    :param data: the cleaned polynomial data.
    :param output_text_file: the text file to write evaluated polynomial expressions to.
    ;returns: output_text_file: the text file to write evaluated polynomial expressions to.
    ;returns: seqList: the circularly linked list of circularly linked lists (list of polynomial expressions)
        of type CSLListOfCSLLists
    """

    global coef         # the temporary coefficient of the current polynomial Node being built
    global xdeg         # the temporary degree of the x-term of the current polynomial Node being built
    global ydeg         # the temporary degree of the y-term of the current polynomial Node being built
    global zdeg         # the temporary degree of the z-term of the current polynomial Node being built
    global newNode      # a boolean flag indicating whether the algorithm should build a new node for the circular singly linked list
    global polyList     # a polynomial circular singly linked lists (type CSLList)
    global seqList      # a linked list of completed polynomial circular singly linked lists (linked list of linked lists) (type CSLListOfCSLLists)
    global count
    global readin_array
    # initialize global variables
    coef = None
    xdeg = None
    ydeg = None
    zdeg = None
    newNode = False
    polyList = None
    seqList = []
    count = 0
    readin_array = data

    # '\n' is the termination key to let algorithm know EOF encountered. If last character is not '\n', add it.
    if readin_array[len(readin_array) - 1] != '\n':
        readin_array.append('\n')

    # the data buffer is clean, so put every character into its respective position in the linked list
    while count < len(readin_array):
        coef = None
        xdeg = None
        ydeg = None
        zdeg = None
        newNode = False
        while not newNode:
            global c            # current character
            global c1           # last character
            c1 = 0
            c = readin_array[count]
            if count > 0:
                c1 = readin_array[count - 1]
            else:
                c1 = 0
            # dictate how operators are handled
            if c in constants.acceptable_operators:
                newNode = True
                if c1 == 'x':
                    xdeg = 1
                if c1 == 'y':
                    ydeg = 1
                if c1 == 'z':
                    zdeg = 1
                if xdeg is None:
                    xdeg = 0
                if ydeg is None:
                    ydeg = 0
                if zdeg is None:
                    zdeg = 0
                if coef is None:
                    coef = 1
                if polyList is None:
                    polyList = CSLList(coef, xdeg, ydeg, zdeg)
                else:
                    polyList += CSLList(coef, xdeg, ydeg, zdeg)
                    count += 1
                    break
                # coef = None
                # xdeg = None
                # ydeg = None
                # zdeg = None
            # dictate how coefficients are handled
            elif count == 0 or c1 in constants.acceptable_operators or c1 == '\n':
                if c in constants.acceptable_coeffs:
                    coef = int(c)
                else:
                    coef = 1
                if c1 == '-':
                    coef *= -1
            elif c in constants.acceptable_coeffs and c1 in constants.acceptable_coeffs:
                coef0 = str(coef) + str(c)
                coef = int(coef0)
            # dictate how to 'x', 'y', and 'z' characters are handled
            elif c in constants.acceptable_degs and c1 in constants.acceptable_operands:
                # cover cases in which no parameter is defined (ie xy or yz) and default to 0
                if c1 == 'x':
                    xdeg = int(c)
                elif c1 == 'y':
                    ydeg = int(c)
                    if xdeg is None:
                        xdeg = 0
                elif c1 == 'z':
                    zdeg = int(c)
                    if xdeg is None:
                        xdeg = 0
                    if ydeg is None:
                        ydeg = 0
            elif c1 in constants.acceptable_operands:
                # cover cases in which no exponent is defined (ie xyz) and default to 1
                if c1 == 'x':
                    xdeg = 1
                elif c1 == 'y':
                    ydeg = 1
                    if xdeg is None:
                        xdeg = 0
                elif c1 == 'z':
                    zdeg = 1
                    if xdeg is None:
                        xdeg = 0
                    if ydeg is None:
                        ydeg = 0
                # the last character was an x, y, or z term that did not have a degree (ie 3xyz where z is implict degree of 1)
                # handle it
                if c == '\n':
                    newNode = True
                    newNode = True
                    if xdeg is None:
                        xdeg = 0
                    if ydeg is None:
                        ydeg = 0
                    if zdeg is None:
                        zdeg = 0
                    if polyList is None:
                        polyList = CSLList(coef, xdeg, ydeg, zdeg)
                        seqList.append(polyList)
                        polyList = None
                        count += 1
                        break
                    else:
                        polyList += CSLList(coef, xdeg, ydeg, zdeg)
                        seqList.append(polyList)
                        polyList = None
                        count += 1
                        break
            # dictate how new lines are handled
            elif c == '\n':
                newNode = True
                newNode = True
                if xdeg is None:
                    xdeg = 0
                if ydeg is None:
                    ydeg = 0
                if zdeg is None:
                    zdeg = 0
                # this is a single-term polynomial
                if polyList is None:
                    polyList = CSLList(coef, xdeg, ydeg, zdeg)
                    seqList.append(polyList)
                    polyList = None
                    count += 1
                    break
                # multi-term polynomial
                else:
                    polyList += CSLList(coef, xdeg, ydeg, zdeg)
                    seqList.append(polyList)
                    polyList = None
                    count += 1
                    break
            # counter to ensure we don't violate the max or min indices of the data buffer
            count += 1

    return seqList, output_text_file


def evaluateAndDisplayPolynomials(seqList, output_text_file):
    """
    Takes the linked list of circularly singly linked lists (the polynomial data represented as linked lists) and performs
        the required mathematical operations on them.
    Upon completion of the mathematical operations, a number of evaluations are performed on the resulting polynomials with
        integer values of x, y, and z.
    Prints the results of the mathematical operations on each read polynomials to the screen and writes identical output
     to the specified output file.
    Prints the results of the polynomial evaluations on each read polynomials to the screen and writes identical output
     to the specified output file.
    :param seqList: type: CSLListOfCSLliststhe linked list (list of polynomial sequences) of circular singly linked lists
     (individual polynomial sequences of multiple polynomial terms).
    :param output_text_file: the text file to write evaluated polynomial expressions to.
    """
    # open the output file and build a header for aesthetic appearance
    output_text_file = open(str(output_text_file), 'a')
    output_text_file.truncate(0)
    output_text_file.write(f'*****************************************************************************************\n')
    output_text_file.write(f'*****************************************************************************************\n')
    output_text_file.write(f'*****************************************************************************************\n')
    output_text_file.write(f'\t\t\t\t\t\t\t\t\t\tWelcome\n')
    output_text_file.write(f'*****************************************************************************************\n')
    output_text_file.write(f'\t\t\t\t\t\tStarting Polynomial Conversion Program\n')
    output_text_file.write(f'*****************************************************************************************\n')

    # let the user know how many expressions were found in the input file
    output_text_file.write(f'\t{len(seqList)} total polynomials were read in\n')
    output_text_file.write(f'\tBeginning evaluation of polynomials for required operations now...\n\n\n')
    print(f'\t{len(seqList)} total polynomials were read in')
    print(f'\tBeginning evaluation of polynomials for required operations now.\n\n')
    # briefly pause processing so that the user can read the output to the console
    time.sleep(3)

    # let the user know how many polynomials were successfully read from input file
    print(f'{len(seqList)} polynomials were read in:')
    for i in range(0, len(seqList)):
        print(f'({constants.acceptable_chars[i]})')
        print(f'{seqList[i].returnFullList()}')
        output_text_file.write(f'({constants.acceptable_chars[i]})\n')
        output_text_file.write(f'{seqList[i].returnFullList()}\n')
    print('*****************************************************************************************\n')
    output_text_file.write(f'*****************************************************************************************\n')

    time.sleep(3)
    # begin performing mathematical operations on the read-in polynomials
    print(f'The resulting expressions for each required operation are: ')
    global op_counter       # a counter for how many polynomial operations are performed (aim is to give O(n) per polynomial
    op_counter = 0
    # loop over each operation required and perform on the respective set of polynomial CSLLists
    for i in range(0, len(constants.operations_list)):
        current_op = constants.operations_list[i]
        # base cases for each operation to be performed
        # each case performs the following:
        #   1) mathematical operation
        #   2) prints the operands, operation,  and result to the screen
        #   3) writes operands, operation and result to output file
        #   4) counts number of operations performed on each expression
        #   5) prepares each polynomial CSLList for evaluation with integer / floating values
        if current_op == 'A + B':
            op = seqList[0] + seqList[1]
            opList = op.returnFullList()
            print(f'{current_op}:')
            print(f'[{seqList[0].returnFullList()}] + [{seqList[1].returnFullList()}]')
            print('\tevaluates to: ')
            print(f'\t{opList}\n')
            output_text_file.write(f'{current_op}:\n')
            output_text_file.write(f'[{seqList[0].returnFullList()}] + [{seqList[1].returnFullList()}]\n')
            output_text_file.write('\tevaluates to: \n')
            output_text_file.write(f'\t{opList}\n\n')
        elif current_op == 'A + C' and len(seqList) > 2:
            op = seqList[0] + seqList[2]
            opList = op.returnFullList()
            print(f'{current_op}:')
            print(f'[{seqList[0].returnFullList()}] + [{seqList[2].returnFullList()}]')
            print('\tevaluates to: ')
            print(f'\t{opList}\n')
            output_text_file.write(f'{current_op}:\n')
            output_text_file.write(f'[{seqList[0].returnFullList()}] + [{seqList[2].returnFullList()}]\n')
            output_text_file.write('\tevaluates to: \n')
            output_text_file.write(f'\t{opList}\n\n')
        elif current_op == 'A + D' and len(seqList) > 3:
            op = seqList[0] + seqList[3]
            opList = op.returnFullList()
            print(f'{current_op}:')
            print(f'[{seqList[0].returnFullList()}] + [{seqList[3].returnFullList()}]')
            print('\tevaluates to: ')
            print(f'\t{opList}\n')
            output_text_file.write(f'{current_op}:\n')
            output_text_file.write(f'[{seqList[0].returnFullList()}] + [{seqList[3].returnFullList()}]\n')
            output_text_file.write('\tevaluates to: \n')
            output_text_file.write(f'\t{opList}\n\n')
        elif current_op == 'B + C' and len(seqList) > 2:
            op = seqList[1] + seqList[2]
            opList = op.returnFullList()
            print(f'{current_op}:')
            print(f'[{seqList[1].returnFullList()}] + [{seqList[2].returnFullList()}]')
            print('\tevaluates to: ')
            print(f'\t{opList}\n')
            output_text_file.write(f'{current_op}:\n')
            output_text_file.write(f'[{seqList[1].returnFullList()}] + [{seqList[2].returnFullList()}]\n')
            output_text_file.write('\tevaluates to: \n')
            output_text_file.write(f'\t{opList}\n\n')
        elif current_op == 'B + D' and len(seqList) > 3:
            op = seqList[1] + seqList[3]
            opList = op.returnFullList()
            print(f'{current_op}:')
            print(f'[{seqList[1].returnFullList()}] + [{seqList[3].returnFullList()}]')
            print('\tevaluates to: ')
            print(f'\t{opList}\n')
            output_text_file.write(f'{current_op}:\n')
            output_text_file.write(f'[{seqList[1].returnFullList()}] + [{seqList[3].returnFullList()}]\n')
            output_text_file.write('\tevaluates to: \n')
            output_text_file.write(f'\t{opList}\n\n')
        elif current_op == 'C + D' and len(seqList) > 3:
            op = seqList[2] + seqList[3]
            opList = op.returnFullList()
            print(f'{current_op}:')
            print(f'[{seqList[2].returnFullList()}] + [{seqList[3].returnFullList()}]')
            print('\tevaluates to: ')
            print(f'\t{opList}\n')
            output_text_file.write(f'{current_op}:\n')
            output_text_file.write(f'[{seqList[2].returnFullList()}] + [{seqList[3].returnFullList()}]\n')
            output_text_file.write('\tevaluates to: \n')
            output_text_file.write(f'\t{opList}\n\n')
        elif current_op == 'B - A':
            op = seqList[1] - seqList[0]
            opList = op.returnFullList()
            print(f'{current_op}:')
            print(f'[{seqList[1].returnFullList()}] - [{seqList[0].returnFullList()}]')
            print('\tevaluates to: ')
            print(f'\t{opList}\n')
            output_text_file.write(f'{current_op}:\n')
            output_text_file.write(f'[{seqList[1].returnFullList()}] - [{seqList[0].returnFullList()}]\n')
            output_text_file.write('\tevaluates to: \n')
            output_text_file.write(f'\t{opList}\n\n')
        elif current_op == 'B - D' and len(seqList) > 3:
            op = seqList[1] - seqList[3]
            opList = op.returnFullList()
            print(f'{current_op}:')
            print(f'[{seqList[1].returnFullList()}] - [{seqList[3].returnFullList()}]')
            print('\tevaluates to: ')
            print(f'\t{opList}\n')
            output_text_file.write(f'{current_op}:\n')
            output_text_file.write(f'[{seqList[1].returnFullList()}] - [{seqList[3].returnFullList()}]\n')
            output_text_file.write('\tevaluates to: \n')
            output_text_file.write(f'\t{opList}\n\n')
        elif current_op == 'A * B':
            op = seqList[0] - seqList[1]
            opList = op.returnFullList()
            print(f'{current_op}:')
            print(f'[{seqList[0].returnFullList()}] * [{seqList[1].returnFullList()}]')
            print('\tevaluates to: ')
            print(f'\t{opList}\n')
            output_text_file.write(f'{current_op}:\n')
            output_text_file.write(f'[{seqList[0].returnFullList()}] * [{seqList[1].returnFullList()}]\n')
            output_text_file.write('\tevaluates to: \n')
            output_text_file.write(f'\t{opList}\n\n')
        elif current_op == 'A * C' and len(seqList) > 2:
            op = seqList[0] * seqList[2]
            opList = op.returnFullList()
            print(f'{current_op}:')
            print(f'[{seqList[0].returnFullList()}] * [{seqList[2].returnFullList()}]')
            print('\tevaluates to: ')
            print(f'\t{opList}\n')
            output_text_file.write(f'{current_op}:\n')
            output_text_file.write(f'[{seqList[0].returnFullList()}] * [{seqList[2].returnFullList()}]\n')
            output_text_file.write('\tevaluates to: \n')
            output_text_file.write(f'\t{opList}\n\n')
        elif current_op == 'A * D' and len(seqList) > 3:
            op = seqList[0] * seqList[3]
            opList = op.returnFullList()
            print(f'{current_op}:')
            print(f'[{seqList[0].returnFullList()}] * [{seqList[3].returnFullList()}]')
            print('\tevaluates to: ')
            print(f'\t{opList}\n')
            output_text_file.write(f'{current_op}:\n')
            output_text_file.write(f'[{seqList[0].returnFullList()}] * [{seqList[3].returnFullList()}]\n')
            output_text_file.write('\tevaluates to: \n')
            output_text_file.write(f'\t{opList}\n\n')
        elif current_op == 'B * A':
            op = seqList[1] * seqList[0]
            opList = op.returnFullList()
            print(f'{current_op}:')
            print(f'[{seqList[1].returnFullList()}] * [{seqList[0].returnFullList()}]')
            print('\tevaluates to: ')
            print(f'\t{opList}\n')
            output_text_file.write(f'{current_op}:\n')
            output_text_file.write(f'[{seqList[1].returnFullList()}] * [{seqList[0].returnFullList()}]\n')
            output_text_file.write('\tevaluates to: \n')
            output_text_file.write(f'\t{opList}\n\n')
        elif current_op == 'B * C' and len(seqList) > 2:
            op = seqList[1] * seqList[2]
            opList = op.returnFullList()
            print(f'{current_op}:')
            print(f'[{seqList[1].returnFullList()}] * [{seqList[2].returnFullList()}]')
            print('\tevaluates to: ')
            print(f'\t{opList}\n')
            output_text_file.write(f'{current_op}:\n')
            output_text_file.write(f'[{seqList[1].returnFullList()}] * [{seqList[2].returnFullList()}]\n')
            output_text_file.write('\tevaluates to: \n')
            output_text_file.write(f'\t{opList}\n\n')
        elif current_op == 'B * D' and len(seqList) > 3:
            op = seqList[1] * seqList[3]
            opList = op.returnFullList()
            print(f'{current_op}:')
            print(f'[{seqList[1].returnFullList()}] * [{seqList[3].returnFullList()}]')
            print('\tevaluates to: ')
            print(f'\t{opList}\n')
            output_text_file.write(f'{current_op}:\n')
            output_text_file.write(f'[{seqList[1].returnFullList()}] * [{seqList[3].returnFullList()}]\n')
            output_text_file.write('\tevaluates to: \n')
            output_text_file.write(f'\t{opList}\n\n')
        elif current_op == 'C * D' and len(seqList) > 3:
            op = seqList[2] * seqList[3]
            opList = op.returnFullList()
            print(f'{current_op}:')
            print(f'[{seqList[2].returnFullList()}] * [{seqList[3].returnFullList()}]')
            print('\tevaluates to: ')
            print(f'\t{opList}\n')
            output_text_file.write(f'{current_op}:\n')
            output_text_file.write(f'[{seqList[2].returnFullList()}] * [{seqList[3].returnFullList()}]\n')
            output_text_file.write('\tevaluates to: \n')
            output_text_file.write(f'\t{opList}\n\n')
        op_counter += 1
        print('-----------------------------------------------------------------------------------------')
        output_text_file.write('-----------------------------------------------------------------------------------------\n')
        time.sleep(1.0)

    # mathematical operations performed on the polynomial CSLLists are complete
    # now evaluate each resulting expression with required integer values from assignment
    print('*****************************************************************************************')
    print('*****************************************************************************************')
    print('\n\nNow performing evaluation of polynomials at required points:\n')
    time.sleep(3.0)
    # a failure counter that is implemented to give the user feedback on which polynomials fail to evaluate
    fail_count = 0
    for i in range(0, len(seqList)):
        for j in range(0, len(constants.eval_points)):
            eval_points = constants.eval_points[j]
            print(f'Polynomial ({constants.acceptable_chars[i]}) evaluated at x = {eval_points[0]}, y = {eval_points[1]}, and z = {eval_points[2]}')
            print(f'\t{seqList[i].returnFullList()} \t-> \t{seqList[i].evaluateList(eval_points[0], eval_points[1], eval_points[2])}')
            print('-----------------------------------------------------------------------------------------')
            output_text_file.write(f'Polynomial ({constants.acceptable_chars[i]}) evaluated at x = {eval_points[0]}, y = {eval_points[1]}, and z = {eval_points[2]}\n')
            output_text_file.write(f'\t{seqList[i].returnFullList()} \t-> \t{seqList[i].evaluateList(eval_points[0], eval_points[1], eval_points[2])}\n')
            output_text_file.write('-----------------------------------------------------------------------------------------\n')
            op_counter += 1
            time.sleep(1.0)
        print('-----------------------------------------------------------------------------------------')
        print('-----------------------------------------------------------------------------------------')
        output_text_file.write('-----------------------------------------------------------------------------------------\n')
        output_text_file.write('-----------------------------------------------------------------------------------------\n')
        time.sleep(2.0)

    # print a footer for UI aesthetics
    print('*****************************************************************************************')
    print('*****************************************************************************************')
    # let the user know how many total expressions passed and failed, written to command-prompt
    print(f'{len(seqList) - fail_count} out of {len(seqList)} total read polynomials were successfully evaluated.')
    print(f'{fail_count} out of {len(seqList)} total read polynomials were unsuccessfully evaluated.')
    print(f'{op_counter} polynomial operations were performed.')
    print('*****************************************************************************************')
    print('*****************************************************************************************')
    print('*****************************************************************************************')
    # write identical output to output file
    output_text_file.write(f'{len(seqList) - fail_count} out of {len(seqList)}  total read  polynomials were successfully evaluated.\n')
    output_text_file.write(f'{fail_count} out of {len(seqList)} total read polynomials were unsuccessfully evaluated.\n')
    output_text_file.write(f'{op_counter} polynomial operations were performed.\n')
    output_text_file.write(
        '*****************************************************************************************\n')
    output_text_file.write(
        '*****************************************************************************************\n')
    output_text_file.write(
        '*****************************************************************************************\n')
    output_text_file.close()





