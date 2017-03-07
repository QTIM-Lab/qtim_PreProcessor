
import os

from subprocess import call

def mri_convert(dicom_volume, output_filename):

	if os.path.isdir(dicom_volume):
		dicom_volume = os.listdir(path)[0]

	mri_convert_base_command = ['mri_convert']

	mri_convert_specific_command = mri_convert_base_command + [dicom_volume, output_filename]

	try:
		print 'Using freesurfer\'s mri_convert to convert DICOM into nifti for file... ' + dicom_volume
		
		call(' '.join(mri_convert_specific_command), shell=True)

	except:
		print 'Converting DICOM into nifti failed for file ' + dicom_volume + 'and output file ' + output_filename

	return

def slicer_convert():
	return

def execute(input_volume, output_filename, specific_function, params):

	if 'specific_function' == 'mri_convert':
		mri_convert(*[input_volume, output_filename] + [params])
	else:
		print 'There is no conversion method associated with this keyword: ' + specific_function + '. Skipping this volume..'


def run_test():
	return

if __name__ == '__main__':
	run_test()