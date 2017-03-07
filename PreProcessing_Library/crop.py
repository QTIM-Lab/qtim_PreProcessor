import os
import glob

from subprocess import call

def crop_with_label(crop_volume, label_volume, output_filename, background_value=0):

	label_data = nifti_util.nifti_2_numpy(label_volume)

	try:
		print 'Using python\'s nibabel package to crop out background voxels on ' + crop_volume + ' using background values from the label at ' + label_volume + '...'
		
		crop_data = nifti_util.nifti_2_numpy(crop_volume)
		crop_data[label_data == 0] = 0
		nifti_util.save_numpy_2_nifti(crop_data, crop_volume, output_filename)

	except:
		print 'Cropping with Python failed for file ' + crop_volume

	return

def execute(input_volume, specific_function, params):

	if 'specific_function' == 'crop_python':
		crop_with_label(params)
	else:
		print 'There is no cropping method associated with this keyword: ' + specific_function + '. Skipping this volume..'

def run_test():
	return

if __name__ == '__main__':
	run_test()