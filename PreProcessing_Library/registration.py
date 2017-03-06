""" This is a wrapper script for BRAINSFit registration by 3D Slicer. In the future, there could be an all-Python
	implementation of registration in this function. In the meantime, one will need 3D Slicer (or a Docker container
	with 3DSlicer inside).
"""

from qtim_tools.qtim_utilities import nifti_util
from subprocess import call

import numpy as np
import glob
import os

def register_to_one(fixed_volume, Slicer_Path, moving_volume_folder, output_suffix = '', output_folder='', file_regex='*.nii*',transform_type='Rigid,ScaleVersor3D,ScaleSkewVersor3D,Affine', transform_mode = 'useMomentsAlign', interpolation_mode = 'Linear', sampling_percentage = .06):

	if output_folder == '':
		output_folder = moving_volume_folder

	BRAINSFit_base_command = [Slicer_Path, '--launch', 'BRAINSFit', '--fixedVolume', '"' + fixed_volume + '"', '--transformType', transform_type, '--initializeTransformMode', transform_mode, '--interpolationMode', interpolation_mode, '--samplingPercentage', str(sampling_percentage)]

	if isinstance(moving_volume_folder, basestring):
		moving_volumes = glob.glob(moving_volume_folder + file_regex)
	else:
		moving_volumes = []
		for folder in moving_volume_folder:
			moving_volumes += glob.glob(folder + file_regex)


	for moving_volume in moving_volumes:

		if os.path.normpath(moving_volume) == os.path.normpath(fixed_volume):
			continue

		no_path = os.path.basename(os.path.normpath(moving_volume))
		file_prefix = str.split(no_path[-1], '.')[0]

		output_filename = output_folder + file_prefix + output_suffix + '.' + '.'.join(file_prefix[1:-1])

		BRAINSFit_specific_command = BRAINSFit_base_command + ['--movingVolume','"' + no_path[0] +  '/' + no_path[1] + '"','--outputVolume','"' + output_filename + '"']

		try:
			print 'Using 3DSlicer\'s BRAINSFit to register ' + moving_volume + ' to ' + fixed_volume + '...'
			call(' '.join(BRAINSFit_specific_command), shell=True)
		except:
			pass

	return

def run_test():

	Slicer_Path = '"C:/Users/azb22/Documents/Software/SlicerNightly/Slicer 4.6.0/Slicer.exe"'
	fixed_volume = 'C:/Users/azb22/Documents/Scripting/Tata_Hospital/Drawn_ROI_TestFiles/7_Ax_T2_PROPELLER.nii.gz'
	moving_folder = 'C:/Users/azb22/Documents/Scripting/Tata_Hospital/Drawn_ROI_TestFiles/'
	output_folder = 'C:/Users/azb22/Documents/Scripting/Tata_Hospital/Drawn_ROI_TestFiles/Registered_Volumes/'

	register_to_one(fixed_volume, Slicer_Path, moving_folder, '_r_T2',output_folder)

	return

if __name__ == "__main__":
	run_test()