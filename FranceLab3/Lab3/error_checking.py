#error_checking.py
#Kordel France
########################################################################################################################
#This file performs file checking operations for the input and output file specified by the user in the command line.
#If necessary, project directories are searched and the I/O files are moved to the appropriate folders.
########################################################################################################################

import os
import shutil

def check_project_for_input_file_in_correct_directory() -> bool:
    """
    Checks to see if the input file is located in the 'io_files' directory.
    :return: a boolean value indicating whether or not the file exists in the correct directory.
    """
    dir_path = os.listdir('io_files')
    found = False
    for item in dir_path:
        if item == 'input.txt':
            found = True
    if not found:
        check_project_for_input_file()
    return found


def check_project_for_input_file() -> bool:
    """
    Checks to see if the input file is located in the project at all.
    :return: a boolean value indicating whether or not the file exists in the project.
    """
    dir_path = os.path.curdir
    found = False
    for item in dir_path:
        if item == 'input.txt':
            # input_file_path = os.path.join(dir_path, item)
            found = True
    if not found:
        for sub_dir in dir_path:
            if not sub_dir.endswith('.idea') and not sub_dir.endswith('.md'):
                for item in os.listdir(os.path.join(sub_dir)):
                    if item == 'input.txt':
                        found = True
    return found


def find_input_file():
    """
    Finds the input file and moves it to the correct directory, 'io_files.'
    :return: the incorrect path the input file was found at for feedback to user.
    """
    dir_path = os.path.curdir
    input_file_path = ''
    found = False
    for item in dir_path:
        if item == 'input.txt':
            input_file_path = os.path.join(dir_path, item)
            found = True
    if not found:
        for sub_dir in dir_path:
            if not sub_dir.endswith('.idea') and not sub_dir.endswith('.md'):
                for item in os.listdir(os.path.join(sub_dir)):
                    if item == 'input.txt':
                        input_file_path = os.path.join(sub_dir, item)
                        shutil.copy(input_file_path, os.path.join('io_files', item))
                        os.remove(os.path.join(sub_dir, item))
    return input_file_path


def check_project_for_output_file_in_correct_directory() -> bool:
    """
    Checks to see if the output file is located in the 'io_files' directory.
    :return: a boolean value indicating whether or not the file exists in the correct directory.
    """
    dir_path = os.listdir('io_files')
    found = False
    for item in dir_path:
        if item == 'output.txt':
            found = True
    if not found:
        check_project_for_output_file()
    return found


def check_project_for_output_file() -> bool:
    """
    Checks to see if the output file is located in the project at all.
    :return: a boolean value indicating whether or not the file exists in the project.
    """
    dir_path = os.path.curdir
    found = False
    for item in dir_path:
        if item == 'output.txt':
            found = True
    if not found:
        for sub_dir in dir_path:
            if not sub_dir.endswith('.idea') and not sub_dir.endswith('.md'):
                for item in os.listdir(os.path.join(sub_dir)):
                    if item == 'output.txt':
                        found = True
    return found


def find_output_file():
    """
    Finds the input file and moves it to the correct directory, 'io_files.'
    :return: the incorrect path the input file was found at for feedback to user.
    """
    dir_path = os.path.curdir
    output_file_path = ''
    found = False
    for item in dir_path:
        if item == 'output.txt':
            output_file_path = os.path.join(dir_path, item)
            found = True
    if not found:
        for sub_dir in dir_path:
            if not sub_dir.endswith('.idea') and not sub_dir.endswith('.md'):
                for item in os.listdir(os.path.join(sub_dir)):
                    if item == 'output.txt':
                        output_file_path = os.path.join(sub_dir, item)
                        shutil.copy(output_file_path, os.path.join('io_files', item))
                        os.remove(os.path.join(sub_dir, item))
    return output_file_path
