import Scripts.Slicer_Import_Dicom

import os
import inspect

from subprocess import call, check_output


def mri_convert(dicom_folder, output_filename):

    if os.path.isdir(dicom_folder):
        dicom_volume = os.path.join(dicom_folder, os.listdir(dicom_folder)[0])

    mri_convert_base_command = ['mri_convert']

    mri_probedicom_patient_id_command = ['mri_probedicom', '--i', dicom_volume, '--t', '10', '20']
    mri_probedicom_series_description_command = ['mri_probedicom', '--i', dicom_volume, '--t', '08', '103e']

    try:
        print '\n'
        print 'Using freesurfer\'s mri_convert to convert DICOM into nifti for folder... ' + dicom_folder
        
        patient_id = check_output(' '.join(mri_probedicom_patient_id_command))
        series_description = check_output(' '.join(mri_probedicom_series_description_command))

        output_directory = os.path.dirname(output_filename)
        
        mri_convert_specific_command = mri_convert_base_command + [dicom_volume, os.path.join(output_directory, patient_id + '_' + series_description)]

        call(' '.join(mri_convert_specific_command), shell=True)

    except:
        print 'Converting DICOM into nifti failed for file ' + dicom_volume + 'and output file ' + output_filename

    return

def slicer_convert(dicom_folder, output_filename):

    dicom_script_filepath = os.path.normpath(inspect.getfile(Scripts.Slicer_Import_Dicom)).replace('\\','/')
    if '.pyc' in dicom_script_filepath:
        dicom_script_filepath = dicom_script_filepath[0:-1]

    DICOM_import_base_command = ['Slicer', '--no-main-window', '--disable-cli-modules', '--python-script', dicom_script_filepath]
    DICOM_import_specific_command = DICOM_import_base_command + ['-i',os.path.abspath(os.path.normpath(dicom_folder)),'-o',os.path.abspath(os.path.normpath(output_filename))]

    try:
        print '\n'
        print 'Using 3DSlicer\'s Dicom Importer to convert DICOM into nifti for folder... ' + dicom_folder
        call(' '.join(DICOM_import_specific_command), shell=True)
    except:
        print 'Converting DICOM into nifti failed for file ' + dicom_volume + 'and output file ' + output_filename

    return

def execute(input_volume, output_filename, specific_function, params):

    if specific_function == 'freesurfer_mri_convert':
        mri_convert(*[input_volume, output_filename] + params)
    if specific_function == 'slicer_convert':
        slicer_convert(*[input_volume, output_filename] + params)       
    else:
        print 'There is no conversion method associated with this keyword: ' + specific_function + '. Skipping volume located at...' + input_volume


def run_test():
    return

if __name__ == '__main__':
    run_test()