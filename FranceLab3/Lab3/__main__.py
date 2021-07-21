#__main__.py
#Kordel France
########################################################################################################################
#This file launches the Polynomial Evaluation program and sets up file processing.
#The file processes command-line arguments and performs some error checking on the I/O files input by the user.
########################################################################################################################

import argparse
from Lab3.file_processing import process_file_data, buildCircularSinglyLinkedLists, evaluateAndDisplayPolynomials
import Lab3.error_checking as error_checking
import time

#print a header for UI aesthetics
#this same header is output to the file after the output file is specified by the user
print('*****************************************************************************************')
print('*****************************************************************************************')
print('*****************************************************************************************')
print('\t\t\t\t\tWelcome')
print('*****************************************************************************************')
print('*****************************************************************************************')

#construct a parser to accept and parse command-line arguments
parser = argparse.ArgumentParser()
#add the argument for the input file
parser.add_argument('input_file', type=str, default='input.txt',
                    help='path to input file')
#add the argument for the output file
parser.add_argument('output_file', type=str, default='output.txt',
                    help='path to output file')
#declare the arguments as separate variables
parse_args = vars(parser.parse_args())
#initialize input and output files for error checking
input_file = ''
output_file = ''
input_file_args = parse_args['input_file']
output_file_args = parse_args['output_file']

#error handling for input file
if input_file_args != None:

    #verify that the input file the user specified is in 'io_files' directory.
    if error_checking.check_project_for_input_file_in_correct_directory() == True:
        input_file = f'io_files/{input_file_args}'

    #if specified input file exists, but in wrong directory, move it to correct directory
    elif error_checking.check_project_for_input_file() == True:
        input_file = error_checking.find_input_file()
        print(f'Your input file was placed in the incorrect spot and it was found at the following path: {input_file}')
        print(f'The program relocated your file to io_files/{input_file_args}.')
        print(f'Please place your input file in the "files" folder from now on.\n')
        input_file = f'io_files/{input_file_args}'

    #if specified input file does not exist, create one for user with demonstration data
    else:
        input_file = 'io_files/input.txt'
        demo_write = open(str(input_file), 'a')
        demo_write.write('5x2y2z3 + 2x1y0z4 + 1x0y2z1 + 1x0y0z1\n3x4y4z4 + 12x3 + y2z2 + 2yz3\n2xyz\n25xyz - 3xz4- 12yz3\n'
                         'x0y1z2\nx1y2z3\nx2y1z0\nx4y-1z-4\n')
        demo_write.close()
        print(f'The {input_file_args} file you specified was not found in this project, so one was created for you at '
              f'the following path: {input_file}')
        print('A few prefix expressions have been provided to start. You may delete them and input your own.\n')

#user did not give proper command line arguments, so search for an 'input.txt' file
elif error_checking.check_project_for_input_file() == True:

    input_file = error_checking.find_input_file()
    print(f'Your input file was placed in the incorrect spot and it was found at the following path: {input_file}')
    print(f'Please place your input file in the "files" folder from now on.\n')

#user gave improper command line arguments and no 'input.txt' file found.
#create input file for them.
else:

    input_file = 'io_files/input.txt'
    demo_write = open(str(input_file), 'a')
    demo_write.close()
    print(f'The {input_file_args} file you specified was not found in this project, so one was created for you at '
              f'the following path: {input_file}')
    print('A few prefix expressions have been provided to start. Delete them and input your own.\n')

#error handling for output file
if output_file_args != None:

    #verify that the input file the user specified is in 'io_files' directory.
    if error_checking.check_project_for_output_file_in_correct_directory() == True:
        output_file = f'io_files/{output_file_args}'

    # if specified output file exists, but in wrong directory, move it to correct directory
    elif error_checking.check_project_for_output_file() == True:

        output_file = error_checking.find_output_file()
        print(f'Your output file was placed in the incorrect spot and it was found at the following path: {output_file}')
        print(f'The program relocated your file to io_files/{output_file_args}.')
        print(f'Please place your output file in the "files" folder from now on.\n')
        output_file = f'io_files/{output_file_args}'

    #if specified output file does not exist, create one for user
    else:
        output_file = 'io_files/output.txt'
        demo_write = open(str(output_file), 'a')
        demo_write.close()
        print(f'The {output_file_args} file you specified was not found in this project, so one was created for you at '
              f'the following path: {output_file}\n')

#user gave improper command line arguments and no 'output.txt' file found.
#create output file for them.
else:
    output_file = 'io_files/output.txt'
    print(f'The {output_file_args} file you specified was not found in this project, so one was created for you at '
          f'the following path: {output_file}\n')

#briefly pause processing so the user can read the feedback given to them in the command prompt
time.sleep(3.0)
#build a header for aesthetic appearance
print('*****************************************************************************************')
print('\t\t\t\tStarting Polynomial Conversion Program\n')
print('*****************************************************************************************')

#begin processing the data in the input file and format it for conversion of all prefix expressions
readin_array, output_text_file = process_file_data(input_file, output_file)
seqList, output_text_file = buildCircularSinglyLinkedLists(readin_array, output_text_file)
evaluateAndDisplayPolynomials(seqList, output_text_file)
