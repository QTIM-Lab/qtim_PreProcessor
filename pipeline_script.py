import PreProcessing_Library.pipeline as pipeline

# pipeline.clear_directories(['./Sample_Data/RAW_NIFTI', './Sample_Data/ISOTROPIC_NIFTI', './Sample_Data/BIAS_CORRECTED_NIFTI' ])

# #--------------------------------------------------------------------#
# # DICOM Conversion Step
# #Available methods: 'mri_convert'

# input_files = ['./Sample_Data/TCGA-02-0054']
# input_search_phrase = '*'
# input_exclusion_phrase = ''

# output_folder = './Sample_Data/RAW_NIFTI'
# output_suffix = ''

# method = 'freesurfer_mri_convert'

# extra_parameters = []

# pipeline.execute('dicom_convert', input_files, input_search_phrase, input_exclusion_phrase, output_folder, output_suffix, method, extra_parameters)

# #--------------------------------------------------------------------#

# #--------------------------------------------------------------------#
# # Bias Correction Step
# # Available methods: 'ants_n4_bias'

# input_files = ['./Sample_Data/RAW_NIFTI']
# input_search_phrase = '*.nii*'
# input_exclusion_phrase = ''

# output_folder = './Sample_Data/BIAS_CORRECTED_NIFTI'
# output_suffix = '_nobias'

# method = 'ants_n4_bias'

# extra_parameters = []

# pipeline.execute('bias_correct', input_files, input_search_phrase, input_exclusion_phrase, output_folder, output_suffix, method, extra_parameters)

# #--------------------------------------------------------------------#

# #--------------------------------------------------------------------#
# # Resampling Step
# # Available methods: 'slicer_resample'

# input_files = ['./Sample_Data/BIAS_CORRECTED_NIFTI']
# input_search_phrase = '*.nii*'
# input_exclusion_phrase = ''

# output_folder = './Sample_Data/ISOTROPIC_NIFTI'
# output_suffix = '_isotropic'

# method = 'slicer_resample'

# dimensions = [1,1,1]
# interpolation_mode = 'linear'
# extra_parameters = [dimensions, interpolation_mode]

# pipeline.execute('resample', input_files, input_search_phrase, input_exclusion_phrase, output_folder, output_suffix, method, extra_parameters)

#--------------------------------------------------------------------#

#--------------------------------------------------------------------#
# Registration Step
# Available methods: 'slicer_registration'

input_files = ['./Sample_Data/ISOTROPIC_NIFTI']
input_search_phrase = '*.nii*'
input_exclusion_phrase = ''

output_folder = './Sample_Data/REGISTERED_NIFTI'
output_suffix = '_r_27'

method = 'slicer_registration'

fixed_volume = ''
fixed_volume_search_phrase = '*2764*'
transform_type='Rigid,ScaleVersor3D,ScaleSkewVersor3D,Affine'
transform_mode = 'useMomentsAlign'
interpolation_mode = 'Linear'
sampling_percentage = .06
extra_parameters = [fixed_volume, transform_type, transform_mode, interpolation_mode, sampling_percentage]

pipeline.execute('register', input_files, input_search_phrase, input_exclusion_phrase, output_folder, output_suffix, method, extra_parameters)

#--------------------------------------------------------------------#

#--------------------------------------------------------------------#
# Skull-Stripping Step
# Available methods: 'fsl_skull_stripping'

input_files = ['./Sample_Data/REGISTERED_NIFTI']
input_search_phrase = '*2764*.nii*'
input_exclusion_phrase = ''

output_folder = './Sample_Data/SKULLSTRIP_NIFTI'
output_suffix = '_skullstripped'

method = 'fsl_skull_stripping'

output_mask_suffix = '_mask'
skull_strip_threshold=.5
skull_strip_vertical_gradient=0
extra_parameters = [skull_strip_threshold, skull_strip_vertical_gradient]

pipeline.execute('skull_strip', input_files, input_search_phrase, input_exclusion_phrase, output_folder, output_suffix, method, extra_parameters)

#--------------------------------------------------------------------#

#--------------------------------------------------------------------#
# Cropping Step
# Available methods: 'python_crop'

input_files = ['./Sample_Data/REGISTERED_NIFTI']
input_search_phrase = '*2764*.nii*'
input_exclusion_phrase = ''

output_folder = './Sample_Data/SKULLSTRIP_NIFTI'
output_suffix = '_skullstripped'

method = 'python_crop'

label_volume = ''
label_volume_search_phrase = '*2764*mask*.nii*'
extra_parameters = [skull_strip_threshold, skull_strip_vertical_gradient]

pipeline.execute('skull_strip', input_files, input_search_phrase, input_exclusion_phrase, output_folder, output_suffix, method, extra_parameters)

#--------------------------------------------------------------------#