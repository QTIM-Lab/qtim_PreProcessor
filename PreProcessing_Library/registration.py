""" This is a wrapper script for BRAINSFit registration by 3D Slicer. In the future, there could be an all-Python
    implementation of registration in this function. In the meantime, one will need 3D Slicer (or a Docker container
    with 3DSlicer inside).
"""

from subprocess import call
from shutil import copyfile

import glob
import os

def BRAINSFit_register(moving_volume, output_filename, fixed_volume, fixed_volume_search_phrase, transform_type='Rigid,ScaleVersor3D,ScaleSkewVersor3D,Affine', transform_mode = 'useMomentsAlign', interpolation_mode = 'Linear', sampling_percentage = .06):

    if fixed_volume == '' and fixed_volume_search_phrase != '':
        fixed_volume_results = glob.glob(os.path.join(os.path.dirname(moving_volume), fixed_volume_search_phrase))
        if len(fixed_volume_results) == 1:
            fixed_volume = fixed_volume_results[0]
        else:
            print 'Error! Search phrase for fixed registration volume returned either no or multiple results. Cancelling registration, results printed below...'
            print fixed_volume_results
            return

    if fixed_volume == moving_volume:
        print 'Cannot register a volume to itself! Copying over and skipping this volume...'
        copyfile(fixed_volume, output_filename)
        return

    BRAINSFit_base_command = ['Slicer', '--launch', 'BRAINSFit', '--fixedVolume', '"' + fixed_volume + '"', '--transformType', transform_type, '--initializeTransformMode', transform_mode, '--interpolationMode', interpolation_mode, '--samplingPercentage', str(sampling_percentage)]

    BRAINSFit_specific_command = BRAINSFit_base_command + ['--movingVolume',moving_volume,'--outputVolume',output_filename]

    try:
        print '\n'
        print 'Using 3DSlicer\'s BRAINSFit to register ' + moving_volume + ' to ' + fixed_volume + '...'
        call(' '.join(BRAINSFit_specific_command), shell=True)
    except:
        print 'BRAINSFit failed for file ' + moving_volume

    return

def execute(input_volume, output_filename, specific_function, params):

    if specific_function == 'slicer_registration':
        BRAINSFit_register(*[input_volume, output_filename] + params)
    else:
        print 'There is no registration method associated with this keyword: ' + specific_function + '. Skipping volume located at...' + input_volume

def run_test():

    Slicer_Path = '"C:/Users/azb22/Documents/Software/SlicerNightly/Slicer 4.6.0/Slicer.exe"'
    fixed_volume = 'C:/Users/azb22/Documents/Scripting/Tata_Hospital/Drawn_ROI_TestFiles/7_Ax_T2_PROPELLER.nii.gz'
    moving_folder = 'C:/Users/azb22/Documents/Scripting/Tata_Hospital/Drawn_ROI_TestFiles/'
    output_folder = 'C:/Users/azb22/Documents/Scripting/Tata_Hospital/Drawn_ROI_TestFiles/Registered_Volumes/'

    register_to_one(fixed_volume, Slicer_Path, moving_folder, '_r_T2',output_folder)

    return

if __name__ == "__main__":
    run_test()
