from suprocess import call
from qtim_tools.qtim_utilities import nifti_util

import numpy as np
import nibabel as nib

def normalize_zeromean_unitvariance(normalize_volume, ROI_volume='', output_file=''):

	try:
		print 'Using python\'s Nibabel and Numpy packages to normalize intensities within a region of interest to zero mean and unit variance on volume ' + normalize_volume + ' to output volume ' + output_filename + '...'

		normalize_numpy = nifti_util.nifti_2_numpy(normalize_volume)

		if ROI == '':
			vol_mean = np.mean(normalize_numpy)
			vol_std = np.std(normalize_numpy)			
		else:
			ROI_nifti = nifti_util.nifti_2_numpy(ROI_volume)
			vol_mean = np.mean(normalize_numpy[ROI_numpy > 0])
			vol_std = np.std(normalize_numpy[ROI_numpy > 0])

		normalize_numpy = (normalize_numpy - vol_mean) / vol_std

		nifti_util.save_numpy_2_nifti(normalize_numpy, normalize_volume, output_filename)

	except:
		print 'Zero mean and unit variance normalization failed for file ' + normalize_volume
		pass

	return

def execute(input_volume, specific_function, params):

	if 'specific_function' == 'zeromean':
		normalize_zeromean_unitvariance(params)
	else:
		print 'There is no normalization method associated with this keyword: '  + specific_function +  '. Skipping this volume..'

def run_test():
	return

if __name__ == '__main__':
	run_test()