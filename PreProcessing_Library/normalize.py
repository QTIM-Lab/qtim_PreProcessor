from subprocess import call
from qtim_tools.qtim_utilities import nifti_util

import numpy as np
import nibabel as nib

def normalize_zeromean_unitvariance(normalize_volume, output_filename, label_volume='', label_volume_search_phrase=''):

	if label_volume == '' and label_volume_search_phrase != '':
		label_volume_results = glob.glob(os.path.join(os.path.dirname(crop_volume), label_volume_search_phrase))
		if len(label_volume_results) == 1:
			label_volume = label_volume_results[0]
		else:
			print 'Error! Search phrase for skullstripping mask returned multiple results. Cancelling registration, results printed below...'
			print label_volume_results
			return

	try:
		print 'Using python\'s Nibabel and Numpy packages to normalize intensities within a region of interest to zero mean and unit variance on volume ' + normalize_volume + ' to output volume ' + output_filename + '...'

		normalize_numpy = nifti_util.nifti_2_numpy(normalize_volume)

		if label_volume == '':
			vol_mean = np.mean(normalize_numpy)
			vol_std = np.std(normalize_numpy)			
		else:
			ROI_nifti = nifti_util.nifti_2_numpy(label_volume)
			vol_mean = np.mean(normalize_numpy[ROI_numpy > 0])
			vol_std = np.std(normalize_numpy[ROI_numpy > 0])

		normalize_numpy = (normalize_numpy - vol_mean) / vol_std

		nifti_util.save_numpy_2_nifti(normalize_numpy, normalize_volume, output_filename)

	except:
		print 'Zero mean and unit variance normalization failed for file ' + normalize_volume
		pass

	return

def execute(input_volume, specific_function, params):

	if specific_function == 'zeromean_normalize':
		normalize_zeromean_unitvariance(*[input_volume, output_filename] + params)
	else:
		print 'There is no normalization method associated with this keyword: '  + specific_function +  '. Skipping volume located at...' + input_volume


def run_test():
	return

if __name__ == '__main__':
	run_test()