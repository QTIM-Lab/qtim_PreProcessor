from subprocess import call

def skull_strip_fsl(bet_volume, output_filename, skull_strip_threshold=.5, skull_strip_vertical_gradient=0,):
	
	# Note - include head radius and center options in the future.

	bet_base_command = ['bet2', '-f', str(skull_strip_threshold), '-g', str(skull_strip_vertical_gradient)]

	bet_specific_command = bet_base_command + [bet_volume, output_filename]

	try:
		print 'Using FSL\'s BET2 (Brain Extraction Tool) to skull-strip ' + bet_volume + ' to output volume ' + output_filename + '...'
		call(' '.join(bet_specific_command), shell=True)
	except:
		print 'BET2 skull-stripping failed for file ' + resample_volume

	return

def execute(input_volume, specific_function, params):

	if 'specific_function' == 'bet2':
		skull_strip_fsl(params)
	else:
		print 'There is no skull-stripping method associated with this keyword: ' + specific_function + '. Skipping this volume..'

def run_test():
	return

if __name__ == '__main__':
	run_test()