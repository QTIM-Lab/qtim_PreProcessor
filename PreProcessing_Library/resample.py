import os
import glob

from subprocess import call

def resample_slicer(resample_volume, Slicer_Path, output_filepath, dimensions=[1,1,1], interpolation_mode = 'linear'):

	ResampleVolume_base_command = ['Slicer', '--launch', 'ResampleVolume', '-i', interpolation_mode]

	ResampleVolume_base_command += ['-s', str(dimensions).strip('[] ')]

	ResampleVolume_specific_command = ResampleVolume_base_command + [resample_volume, output_filename]

	try:
		print 'Using 3DSlicer\'s ResampleVolume to resample ' + resample_volume + ' to ' + dimensions + '...'
		call(' '.join(ResampleVolume_specific_command), shell=True)
	except:
		print '3DSlicer\'s resample volume failed for file ' + resample_volume

	return

def execute(input_volume, specific_function, params):

	if 'specific_function' == 'resample_Slicer':
		resample_Slicer(params)
	else:
		print 'There is no resampling method associated with this keyword: ' + specific_function + '. Skipping this volume..'

def run_test():
	return

if __name__ == '__main__':
	run_test()