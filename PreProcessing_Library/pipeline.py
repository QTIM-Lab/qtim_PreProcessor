
import numpy as np
import os
import glob
import re
import fnmatch
import shutil

import normalize
import import_dicom
import crop
import bias_correction
import resample
import skull_strip
import registration

preprocessing_dictionary = {
    'dicom_convert': import_dicom,
    'resample': resample,
    'bias_correct': bias_correction,
    'crop': crop,
    'register': registration,
    'skull_strip': skull_strip,
    'normalize': normalize
}

def grab_files(location_list, file_regex='*', exclusion_regex=''):

    if isinstance(location_list, basestring):
        location_list = [location_list]
    
    output_volumes = []
    for input_volume_item in location_list:
        if os.path.isdir(input_volume_item):
            output_volumes += glob.glob(os.path.join(input_volume_item, file_regex))
        else:
            output_volumes += [input_volume_item]

    if exclusion_regex != '':
        output_volumes = [filepath for filepath in output_volumes if exclusion_regex not in os.path.basename(os.path.normpath(resample_volume))]

    return output_volumes

def grab_folders_recursive(input_folders, file_regex, exclusion_regex):

    if isinstance(input_folders, basestring):
        input_folders = [input_folders]

    output_folders = []

    for input_folder in input_folders:
        
        lowest_dirs = []

        for root,dirs,files in os.walk(input_folder):
            if files and not dirs:
                end_root = os.path.basename(os.path.normpath(root))
                if fnmatch.fnmatch(end_root, file_regex) and (exclusion_regex not in end_root or exclusion_regex == ''):
                    lowest_dirs.append(root)

        output_folders += lowest_dirs

    return output_folders

def grab_output_filepath(input_volume, output_folder, output_suffix = '', make_dir = True):
    
    if output_folder == '':
        output_folder = os.path.dirname(input_volumes)
    elif not os.path.exists(output_folder) and make_dir:
        os.makedirs(output_folder)

    no_path = os.path.basename(os.path.normpath(input_volume))
    file_prefix = str.split(no_path, '.nii')

    output_filename = os.path.join(output_folder, file_prefix[0] + output_suffix + '.nii' + file_prefix[-1])

    return output_filename

def grab_output_filepath_folder(input_volume, output_folder, output_suffix = '', make_dir = True):
    
    if output_folder == '':
        output_folder = os.path.dirname(input_volume)
    elif not os.path.exists(output_folder) and make_dir:
        os.makedirs(output_folder)

    no_path = os.path.basename(os.path.normpath(input_volume))

    output_filename = os.path.join(output_folder, no_path + output_suffix + '.nii.gz')

    return output_filename

def clear_directories(input_directories):

    if isinstance(input_directories, basestring):
        input_directories = [input_directories]

    for directory in input_directories:
        if os.path.isdir(directory):
            shutil.rmtree(directory)

def move_files_recursive(input_filepaths, file_regex='*', exclusion_regex='', output_folder='', output_suffix='', make_dir = True):

    file_list = grab_files(input_filepaths, file_regex, exclusion_regex)

    for move_file in file_list:
        
        output_filepath = grab_output_filepath(move_file, output_folder, output_suffix, make_dir)

        os.rename(move_file, output_filepath)


def execute(preprocess_step, input_files, input_search_phrase, input_exclusion_phrase, output_folder, output_suffix, method, params):

    if preprocess_step == 'dicom_convert':
        input_volumes = grab_folders_recursive(input_files, input_search_phrase, input_exclusion_phrase)
    else:
        input_volumes = grab_files(input_files, input_search_phrase, input_exclusion_phrase)
    
    for single_volume in input_volumes:

        if preprocess_step == 'dicom_convert':
            output_filename = grab_output_filepath_folder(single_volume, output_folder, output_suffix, make_dir=True)
        else:
            output_filename = grab_output_filepath(single_volume, output_folder, output_suffix, make_dir=True)

        preprocessing_dictionary[preprocess_step].execute(single_volume, output_filename, method, params)

    return

def run_test():
    return

if __name__ == '__main__':
    run_test()