import os
import glob

from subprocess import call

def resample_slicer(resample_volume, output_filename, dimensions=[1,1,1], interpolation_mode = 'linear'):

	ResampleVolume_base_command = ['Slicer', '--launch', 'ResampleScalarVolume', '-i', interpolation_mode]

	ResampleVolume_base_command += ['-s', str(dimensions).strip('[]').replace(' ', '')]

	ResampleVolume_specific_command = ResampleVolume_base_command + [resample_volume, output_filename]
	
	print ' '.join(ResampleVolume_specific_command)

	try:
		print '\n'
		print 'Using 3DSlicer\'s ResampleVolume to resample ' + resample_volume + ' to ' + str(dimensions) + '...'
		call(' '.join(ResampleVolume_specific_command), shell=True)
	except:
		print '3DSlicer\'s resample volume failed for file ' + resample_volume

	return

def execute(input_volume, output_filename, specific_function, params):

	if specific_function == 'slicer_resample':
		resample_slicer(*[input_volume, output_filename] + params)
	else:
		print 'There is no resampling method associated with this keyword: ' + specific_function + '. Skipping volume located at...' + input_volume

def run_test():
	return

if __name__ == '__main__':
	run_test()