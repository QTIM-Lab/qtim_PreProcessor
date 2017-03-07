
import os

from subprocess import call

def mri_convert(dicom_folder, output_filename):

	if os.path.isdir(dicom_folder):
		dicom_volume = os.listdir(dicom_folder)[0]

	mri_convert_base_command = ['mri_convert']

	mri_convert_specific_command = mri_convert_base_command + [dicom_volume, output_filename]

	try:
		print '\n'
		print 'Using freesurfer\'s mri_convert to convert DICOM into nifti for folder... ' + dicom_folder
		
		call(' '.join(mri_convert_specific_command), shell=True)

	except:
		print 'Converting DICOM into nifti failed for file ' + dicom_volume + 'and output file ' + output_filename

	return

def slicer_convert():
	return

def execute(input_volume, output_filename, specific_function, params):

	if specific_function == 'freesurfer_mri_convert':
		mri_convert(*[input_volume, output_filename] + params)
	else:
		print 'There is no conversion method associated with this keyword: ' + specific_function + '. Skipping volume located at...' + input_volume


def run_test():
	return

if __name__ == '__main__':
	run_test()