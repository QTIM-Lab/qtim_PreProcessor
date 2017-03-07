import PreProcessing_Library.pipeline as pipeline

#--------------------------------------------------------------------#
# DICOM Conversion Step
# Available methods: 'mri_convert'

# input_files = ['./Sample_Data/TCGA-02-0054']
# input_search_phrase = '*'
# input_exclusion_phrase = ''

# output_folder = './Sample_Data/RAW_NIFTI'
# output_suffix = ''

# method = 'freesurfer_mri_convert'

# extra_parameters = []

# pipeline.execute('dicom_convert', input_files, input_search_phrase, input_exclusion_phrase, output_folder, output_suffix, method, extra_parameters)

#--------------------------------------------------------------------#

#--------------------------------------------------------------------#
# Resampling Step
# Available methods: 'slicer_resample'

input_files = ['./Sample_Data/RAW_NIFTI']
input_search_phrase = '*.nii*'
input_exclusion_phrase = ''

output_folder = './Sample_Data/ISOTROPIC_NIFTI'
output_suffix = '_isotropic'

method = 'slicer_resample'

dimensions = [1,1,1]
interpolation_mode = 'linear'
extra_parameters = [dimensions, interpolation_mode]

pipeline.execute('resample', input_files, input_search_phrase, input_exclusion_phrase, output_folder, output_suffix, method, extra_parameters)

#--------------------------------------------------------------------#

