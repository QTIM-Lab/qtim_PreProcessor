from subprocess import call

import glob
import os
import numpy as np
import common

def normalize_zeromean_unitvariance(normalize_volume, output_filename, label_volume='', label_volume_search_phrase=''):

	if label_volume == '' and label_volume_search_phrase != '':
		label_volume_results = glob.glob(os.path.join(os.path.dirname(normalize_volume), label_volume_search_phrase))
		if len(label_volume_results) == 1:
			label_volume = label_volume_results[0]
		else:
			print 'Error! Search phrase for normalization mask returned multiple results. Cancelling normalization, results printed below...'
			print label_volume_results
			return

	try:
                print '\n'
		print 'Using python\'s Nibabel and Numpy packages to normalize intensities within a region of interest to zero mean and unit variance on volume ' + normalize_volume + ' to output volume ' + output_filename + '...'

		normalize_numpy = common.nifti_2_numpy(normalize_volume)

		if label_volume == '':
			vol_mean = np.mean(normalize_numpy)
			vol_std = np.std(normalize_numpy)			
		else:
			ROI_numpy = common.nifti_2_numpy(label_volume)
			vol_mean = np.mean(normalize_numpy[ROI_numpy > 0])
			vol_std = np.std(normalize_numpy[ROI_numpy > 0])

		normalize_numpy = (normalize_numpy - vol_mean) / vol_std

		common.save_numpy_2_nifti(normalize_numpy, normalize_volume, output_filename)

	except:
		print 'Zero mean and unit variance normalization failed for file ' + normalize_volume
		pass

	return

def execute(input_volume, output_filename, specific_function, params):

	if specific_function == 'zeromean_normalize':
		normalize_zeromean_unitvariance(*[input_volume, output_filename] + params)
	else:
		print 'There is no normalization method associated with this keyword: '  + specific_function +  '. Skipping volume located at...' + input_volume


def run_test():
	return

if __name__ == '__main__':
	run_test()