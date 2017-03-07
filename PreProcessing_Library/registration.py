""" This is a wrapper script for BRAINSFit registration by 3D Slicer. In the future, there could be an all-Python
	implementation of registration in this function. In the meantime, one will need 3D Slicer (or a Docker container
	with 3DSlicer inside).
"""

from subprocess import call

import glob
import os

def BRAINSFit_register(fixed_volume, moving_volume, Slicer_Path, output_filename, transform_type='Rigid,ScaleVersor3D,ScaleSkewVersor3D,Affine', transform_mode = 'useMomentsAlign', interpolation_mode = 'Linear', sampling_percentage = .06):

	if fixed_volume == moving_volume:
		print 'Cannot register a volume to itself! Skipping this volume...'
		return

	BRAINSFit_base_command = [Slicer_Path, '--launch', 'BRAINSFit', '--fixedVolume', '"' + fixed_volume + '"', '--transformType', transform_type, '--initializeTransformMode', transform_mode, '--interpolationMode', interpolation_mode, '--samplingPercentage', str(sampling_percentage)]

	BRAINSFit_specific_command = BRAINSFit_base_command + ['--movingVolume','"' + moving_volume + '"','--outputVolume','"' + output_filename + '"']

	try:
		print 'Using 3DSlicer\'s BRAINSFit to register ' + moving_volume + ' to ' + fixed_volume + '...'
		call(' '.join(BRAINSFit_specific_command), shell=True)
	except:
		print 'BRAINSFit failed for file ' + moving_volume

	return

def execute(input_volume, specific_function, params):

	if 'specific_function' == 'BRAINSFit':
		BRAINSFit_register(params)
	else:
		print 'There is no registration method associated with this keyword: ' + specific_function + '. Skipping this volume..'


def run_test():

	Slicer_Path = '"C:/Users/azb22/Documents/Software/SlicerNightly/Slicer 4.6.0/Slicer.exe"'
	fixed_volume = 'C:/Users/azb22/Documents/Scripting/Tata_Hospital/Drawn_ROI_TestFiles/7_Ax_T2_PROPELLER.nii.gz'
	moving_folder = 'C:/Users/azb22/Documents/Scripting/Tata_Hospital/Drawn_ROI_TestFiles/'
	output_folder = 'C:/Users/azb22/Documents/Scripting/Tata_Hospital/Drawn_ROI_TestFiles/Registered_Volumes/'

	register_to_one(fixed_volume, Slicer_Path, moving_folder, '_r_T2',output_folder)

	return

if __name__ == "__main__":
	run_test()