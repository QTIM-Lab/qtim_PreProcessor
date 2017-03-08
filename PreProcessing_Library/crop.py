import os
import glob
import common

from subprocess import call


def crop_with_label(crop_volume, output_filename, label_volume, label_volume_dir, label_volume_search_phrase, background_value=0):

        if label_volume_dir == '':
            label_volume_dir = os.path.dirname(crop_volume)

	if label_volume == '' and label_volume_search_phrase != '':
		label_volume_results = glob.glob(os.path.join(label_volume_dir, label_volume_search_phrase))
		if len(label_volume_results) == 1:
			label_volume = label_volume_results[0]
		else:
			print 'Error! Search phrase for cropping mask returned multiple or no results. Cancelling cropping, results printed below...'
			print label_volume_results
			return

	label_data = common.nifti_2_numpy(label_volume)

	try:
                print '\n'
		print 'Using python\'s nibabel package to crop out background voxels on ' + crop_volume + ' using background values from the label at ' + label_volume + '...'
		
		crop_data = common.nifti_2_numpy(crop_volume)
		crop_data[label_data == 0] = 0
		common.save_numpy_2_nifti(crop_data, crop_volume, output_filename)

	except:
		print 'Cropping with Python failed for file ' + crop_volume

	return

def execute(input_volume, output_filename, specific_function, params):

	if specific_function == 'python_crop':
		crop_with_label(*[input_volume, output_filename] + params)
	else:
		print 'There is no cropping method associated with this keyword: ' + specific_function + '. Skipping volume located at...' + input_volume

def run_test():
	return

if __name__ == '__main__':
	run_test()