from subprocess import call

def N4_Bias_Correct(n4bias_volume, skull_strip_threshold=.5, skull_strip_vertical_gradient=0, output_file=''):
	
	# Note - include head radius and center options in the future.

	n4bias_base_command = ['N4BiasFieldCorrection', '-f', str(skull_strip_threshold), '-g', str(skull_strip_vertical_gradient)]

	n4bias_specific_command = n4bias_base_command + [n4bias_volume, output_filename]

	try:
		print 'Using ANTs\' N4BiasCorrection to correct intensity inhomgeneities from ' + n4bias_volume + ' to output volume ' + output_filename + '...'
		call(' '.join(n4bias_specific_command), shell=True)
	except:
		print 'ANTs N4BiasCorrection failed for file ' + n4bias_volume
		pass

	return

def execute(input_volume, specific_function, params):

	if 'specific_function' == 'N4':
		N4_Bias_Correct(params)
	else:
		print 'There is no bias correction program associated with this keyword: '  + specific_function +  '. Skipping this volume..'

def run_test():
	return

if __name__ == '__main__':
	run_test()