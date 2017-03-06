
import glob
import os

def grab_files(location_list, file_regex='*', exclusion_regex=''):


	if isinstance(location_list, basestring):
		location_list = [location_list]
	
	output_volumes = []
	for input_volume_item in location_list:
		if os.path.isdir(input_volume_item):
			output_volumes += glob.glob(os.path.join(input_volume_item + file_regex))
		else:
			output_volumes += [input_volume_item]

	if exclusion_regex != '':
		output_volumes = [filepath for filepath in output_volumes if exclusion_regex not in os.path.basename(os.path.normpath(resample_volume))]

	return output_volumes

def grab_output_filepath(input_volume, output_folder, output_suffix = '', make_dir = True):
	
	if output_folder == '':
		output_folder = os.path.dirname(input_volumes)
	elif not os.path.exists(output_folder) and make_dir
		os.makedirs(output_folder)

	no_path = os.path.basename(os.path.normpath(n4bias_volume))
	file_prefix = str.split(no_path[-1], '.')[0]

	output_filename = os.path.join(output_folder, file_prefix + output_suffix + '.' + '.'.join(file_prefix[1:-1]))

	return output_filename

def run_test():
	return

if __name__ == '__main__':
	run_test()