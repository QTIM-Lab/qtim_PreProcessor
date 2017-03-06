
import os
import glob
from common import grab_files

def resample_slicer(input_volumes, Slicer_Path, dimensions=[1,1,1], output_suffix = '', output_folder='', file_regex='*.nii*', interpolation_mode = 'linear'):

	if output_folder == '':
		output_folder = os.path.dirname(input_volumes)

	ResampleVolume_base_command = ['Slicer', '--launch', 'ResampleVolume', '-i', interpolation_mode]

	ResampleVolume_base_command += ['-s', str(dimensions).strip('[] ')]

	resample_volumes = grab_files(input_volumes, file_regex)

	for resample_volume in resample_volumes:

		no_path = os.path.basename(os.path.normpath(resample_volume))
		file_prefix = str.split(no_path[-1], '.')[0]

		output_filename = os.path.join(output_folder, file_prefix + output_suffix + '.' + '.'.join(file_prefix[1:-1]))

		ResampleVolume_specific_command = ResampleVolume_base_command + [resample_volume, output_filename]

		try:
			print 'Using 3DSlicer\'s ResampleVolume to resample ' + resample_volume + ' to ' + dimensions + '...'
			call(' '.join(ResampleVolume_specific_command), shell=True)
		except:
			pass

	return

def run_test():
	return

if __name__ == '__main__':
	run_test()