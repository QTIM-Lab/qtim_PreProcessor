from subprocess import call
import os

def skull_strip_fsl(bet_volume, output_filename, output_mask_suffix='_mask', skull_strip_threshold=.5, skull_strip_vertical_gradient=0):
    
    # Note - include head radius and center options in the future.

    bet_base_command = ['bet2', bet_volume, output_filename, '-f', str(skull_strip_threshold), '-g', str(skull_strip_vertical_gradient), '-m']

    bet_specific_command = bet_base_command

    try:
        print '\n'
        print 'Using FSL\'s BET2 (Brain Extraction Tool) to skull-strip ' + bet_volume + ' to output volume ' + output_filename + '...'
        call(' '.join(bet_specific_command), shell=True)

        no_path = os.path.basename(os.path.normpath(output_filename))
        file_prefix = str.split(no_path, '.nii')
        os.rename(output_filename + '_mask.nii.gz', os.path.join(os.path.dirname(output_filename), file_prefix[0] + output_mask_suffix + '.nii.gz'))

    except:
        print 'BET2 skull-stripping failed for file ' + bet_volume

    return

def execute(input_volume, output_filename, specific_function, params):

    if specific_function == 'fsl_skull_stripping':
        skull_strip_fsl(*[input_volume, output_filename] + params)
    else:
        print 'There is no skull-stripping method associated with this keyword: ' + specific_function + '. Skipping volume located at...' + input_volume

def run_test():
    return

if __name__ == '__main__':
    run_test()