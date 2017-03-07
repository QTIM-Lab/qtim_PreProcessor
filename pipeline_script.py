import PreProcessing_Library.pipeline as pipeline

#--------------------------------------------------------------------#
# DICOM Conversion Steps
# Available methods: 'mri_convert'

input_files = ['/home/QTIM_PreProcess/Sample_Data/TCGA-02-0054']
input_search_phrase = '*'
input_exclusion_phrase = ''

output_folder = 'home/QTIM_PreProcess/Sample_Data/RAW_NIFTI'
output_suffix = ''

method = 'freesurfer_mri_convert'

extra_parameters = []

pipeline.execute('dicom_convert', input_files, input_search_phrase, input_exclusion_phrase, output_folder, output_suffix, method, extra_parameters)

#--------------------------------------------------------------------#

