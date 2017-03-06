
from suprocess import call
from qtim_tools.qtim_utilities import nifti_util

import nibabel as nib

def skull_strip_fsl(input_volumes, skull_strip_threshold=.5, skull_strip_vertical_gradient=0, file_regex='', output_suffix='', output_folder=''):
	
	# Note - include head radius and center options in the future.

	if output_folder == '':
		output_folder = os.path.dirname(input_volumes)

	bet_base_command = ['bet2', '-f', str(skull_strip_threshold), '-g', str(skull_strip_vertical_gradient)]

	bet_volumes = grab_files(input_volumes, file_regex)

	for bet_volume in bet_volumes:

		no_path = os.path.basename(os.path.normpath(bet_volume))
		file_prefix = str.split(no_path[-1], '.')[0]

		output_filename = os.path.join(output_folder, file_prefix + output_suffix + '.' + '.'.join(file_prefix[1:-1]))

		bet_specific_command = bet_base_command + [bet_volume, output_filename]

		try:
			print 'Using FSL\'s BET (Brain Extraction Tool) to skull-strip ' + bet_volume + ' to output volume ' + output_filename + '...'
			call(' '.join(bet_specific_command), shell=True)
		except:
			pass

	return

def crop_with_label(input_volumes, label_volume, file_regex='', output_suffix='', output_folder='', background_value=0)

	# Note - include head radius and center options in the future.

	if output_folder == '':
		output_folder = os.path.dirname(input_volumes)

	crop_volumes = grab_files(input_volumes, file_regex)

	label_data = nifti_util.nifti_2_numpy(label_volume)

	for crop_volume in crop_volumes:

		no_path = os.path.basename(os.path.normpath(crop_volume))
		file_prefix = str.split(no_path[-1], '.')[0]
		
		output_filename = os.path.join(output_folder, file_prefix + output_suffix + '.' + '.'.join(file_prefix[1:-1]))

		try:
			print 'Using python\'s nibabel package to crop out background voxels on ' + crop_volume ' using background values from the label at ' label_volume + '...'
			
			crop_data = nifti_util.nifti_2_numpy(crop_volume)
			crop_data[label_data == 0] = 0
			nifti_util.save_numpy_2_nifti(crop_data, crop_volume, output_filename)

		except:
			pass

	return

def run_test():
	return

if __name__ == '__main__':
	run_test()