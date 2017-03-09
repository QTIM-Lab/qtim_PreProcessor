#--------------------------------------------------------------------#
# Never change this portion, required for functioning in Docker container.
import sys
sys.path.append("..")
import qtim_PreProcessor.PreProcessing_Library.pipeline as pipeline
#--------------------------------------------------------------------#

#--------------------------------------------------------------------#
# DICOM Conversion Step
#Available methods: 'freesurfer_mri_convert'

input_files = ['./INPUT_DATA/TCGA-02-0054']
input_search_phrase = '*'
input_exclusion_phrase = ''

output_folder = './INPUT_DATA/RAW_NIFTI'
output_suffix = ''

method = 'freesurfer_mri_convert'

extra_parameters = []

pipeline.execute('dicom_convert', input_files, input_search_phrase, input_exclusion_phrase, output_folder, output_suffix, method, extra_parameters)

# #--------------------------------------------------------------------#

# #--------------------------------------------------------------------#
# Bias Correction Step
# Available methods: 'ants_n4_bias'

input_files = ['./INPUT_DATA/RAW_NIFTI']
input_search_phrase = '*.nii*'
input_exclusion_phrase = ''

output_folder = './INPUT_DATA/BIAS_CORRECTED_NIFTI'
output_suffix = '_nobias'

method = 'ants_n4_bias'

extra_parameters = []

pipeline.execute('bias_correct', input_files, input_search_phrase, input_exclusion_phrase, output_folder, output_suffix, method, extra_parameters)

#--------------------------------------------------------------------#

#--------------------------------------------------------------------#
# Resampling Step
# Available methods: 'slicer_resample'

input_files = ['./INPUT_DATA/BIAS_CORRECTED_NIFTI']
input_search_phrase = '*.nii*'
input_exclusion_phrase = ''

output_folder = './INPUT_DATA/ISOTROPIC_NIFTI'
output_suffix = '_isotropic'

method = 'slicer_resample'

dimensions = [1,1,1]
interpolation_mode = 'linear'
extra_parameters = [dimensions, interpolation_mode]

pipeline.execute('resample', input_files, input_search_phrase, input_exclusion_phrase, output_folder, output_suffix, method, extra_parameters)

#--------------------------------------------------------------------#

#--------------------------------------------------------------------#
# Registration Step
# Available methods: 'slicer_registration'

input_files = ['./INPUT_DATA/ISOTROPIC_NIFTI']
input_search_phrase = '*.nii*'
input_exclusion_phrase = ''

output_folder = './INPUT_DATA/REGISTERED_NIFTI'
output_suffix = '_r_T2'

method = 'slicer_registration'

fixed_volume = ''
fixed_volume_search_phrase = '*AXT2*'
transform_type='Rigid,ScaleVersor3D,ScaleSkewVersor3D,Affine'
transform_mode = 'useMomentsAlign'
interpolation_mode = 'Linear'
sampling_percentage = .06
extra_parameters = [fixed_volume, fixed_volume_search_phrase, transform_type, transform_mode, interpolation_mode, sampling_percentage]

pipeline.execute('register', input_files, input_search_phrase, input_exclusion_phrase, output_folder, output_suffix, method, extra_parameters)

# #--------------------------------------------------------------------#

# #--------------------------------------------------------------------#
# Skull-Stripping Step
# Available methods: 'fsl_skull_stripping'

input_files = ['./INPUT_DATA/REGISTERED_NIFTI']
input_search_phrase = '*AXT2*.nii*'
input_exclusion_phrase = ''

output_folder = './INPUT_DATA/SKULLSTRIP_NIFTI'
output_suffix = '_skullstripped'

method = 'fsl_skull_stripping'

output_mask_suffix = '_mask'
skull_strip_threshold=.5
skull_strip_vertical_gradient=0
extra_parameters = [output_mask_suffix, skull_strip_threshold, skull_strip_vertical_gradient]

pipeline.execute('skull_strip', input_files, input_search_phrase, input_exclusion_phrase, output_folder, output_suffix, method, extra_parameters)

# #--------------------------------------------------------------------#

# #--------------------------------------------------------------------#
# Cropping Step
# Available methods: 'python_crop'

input_files = ['./INPUT_DATA/REGISTERED_NIFTI']
input_search_phrase = '*.nii*'
input_exclusion_phrase = ''

output_folder = './INPUT_DATA/SKULLSTRIP_NIFTI'
output_suffix = '_skullstripped'

method = 'python_crop'

label_volume = ''
label_volume_dir = './INPUT_DATA/SKULLSTRIP_NIFTI'
label_volume_search_phrase = '*_mask.nii*'
background_value = 0
extra_parameters = [label_volume, label_volume_dir, label_volume_search_phrase, background_value]

pipeline.execute('crop', input_files, input_search_phrase, input_exclusion_phrase, output_folder, output_suffix, method, extra_parameters)

# #--------------------------------------------------------------------#

# #--------------------------------------------------------------------#
# Normalizing Step
# Available methods: 'zeromean_normalize'

input_files = ['./INPUT_DATA/SKULLSTRIP_NIFTI']
input_search_phrase = '*_skullstripped.nii*'
input_exclusion_phrase = ''

output_folder = './INPUT_DATA/NORMALIZED_NIFTI'
output_suffix = '_normalized'

method = 'zeromean_normalize'

label_volume = ''
label_volume_search_phrase = '*_mask.nii*'
extra_parameters = [label_volume, label_volume_search_phrase]

pipeline.execute('normalize', input_files, input_search_phrase, input_exclusion_phrase, output_folder, output_suffix, method, extra_parameters)

# #--------------------------------------------------------------------#

pipeline.move_files_unique_folder(input_filepaths='./INPUT_DATA/NORMALIZED_NIFTI', output_base_directory='./INPUT_DATA', separator='_', prefix_segments=1)
pipeline.clear_directories(['./INPUT_DATA/BIAS_CORRECTED_NIFTI', './INPUT_DATA/ISOTROPIC_NIFTI', './INPUT_DATA/REGISTERED_NIFTI', './INPUT_DATA/SKULLSTRIP_NIFTI', './INPUT_DATA/NORMALIZED_NIFTI'])