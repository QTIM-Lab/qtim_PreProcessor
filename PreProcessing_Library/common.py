
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

def run_test():
	return

if __name__ == '__main__':
	run_test()