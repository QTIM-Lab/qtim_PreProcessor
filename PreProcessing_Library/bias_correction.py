from suprocess import call
from qtim_tools.qtim_utilities import nifti_util

import nibabel as nib

def N4_Bias_Correct(input_volumes, skull_strip_threshold=.5, skull_strip_vertical_gradient=0, file_regex='', output_suffix='', output_folder=''):
	
	# Note - include head radius and center options in the future.

	if output_folder == '':
		output_folder = os.path.dirname(input_volumes)

	n4bias_base_command = ['n4bias2', '-f', str(skull_strip_threshold), '-g', str(skull_strip_vertical_gradient)]

	bias_volumes = grab_files(input_volumes, file_regex)

	for n4bias_volume in n4bias_volumes:

		no_path = os.path.basename(os.path.normpath(n4bias_volume))
		file_prefix = str.split(no_path[-1], '.')[0]

		output_filename = os.path.join(output_folder, file_prefix + output_suffix + '.' + '.'.join(file_prefix[1:-1]))

		n4bias_specific_command = n4bias_base_command + [n4bias_volume, output_filename]

		try:
			print 'Using FSL\'s BET (Brain Extraction Tool) to skull-strip ' + n4bias_volume + ' to output volume ' + output_filename + '...'
			call(' '.join(n4bias_specific_command), shell=True)
		except:
			pass

	return

def run_test():
	return

if __name__ == '__main__':
	run_test()