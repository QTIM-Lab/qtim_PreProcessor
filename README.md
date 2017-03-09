# qtim_PreProcessor
This page contains a Docker container and full code/resources for pre-processing medical imaging data at the Quantitative Tumor Imaging Lab at the Martinos Center (MIT/HST). It aggregates pre-processing steps from 3D Slicer, FreeSurfer, ANTs, and FSL, as well as hard-coded steps written in Python with help from the python package nibabel. Currently, it takes in DICOM files and outputs NIFTI files.

# Usage

Pull the docker container from https://hub.docker.com/r/qtimlab/med-image-preprocessing/.

When run, the container will run its preprocessing pipeline with a user-provided pipeline script titled "pipeline_script.py" on a data directory mounted to the Docker container. For an example pipeline script and data file, try using the "Sample_Data" directory located in this repository.

A sample Docker command would look like:

```
docker run -rm -v ~/Sample_Data:/home/data qtimlab/med-image-preprocessing
```

The "/home/data" portion on the right-hand side of the "-v" option should never change. Running this script will load your pipeline script and, provided you have configured the pipeline for your data, run pre-processing steps and output the data in a new folder. 

## Sample "pipeline_script.py"

This Docker container expects configuration files titled "pipeline_script.py" in the top-level of the mounted directory. "pipeline_script.py" is meant to be a modular and mixable script for creating pipeline steps in whatever order a user desires.

Below, I'll document some of the pipeline script included in this repository at /Sample_Data/pipeline_script.py. That script is meant to take in one patient visit in DICOM format and:

1. Convert each provided volume to Nifti format. Nifti files will be titled according to the "Patient_ID" and "Series_Description" tags in each DICOM header.
2. Perform N4 Bias Correction on each volume to remove intensity inhomogeneities.
3. Resample each volume to 1mm x 1mmm x 1mm isotropic resolution.
4. Register all images to the provided Axial T2 volume.
5. Create a brain mask by performing skull-stripping on the provided Axial T2 volume.
6. Crop all provided images according to the brain mask.7
7. Normalize intensities within the brain mask to a zero mean and unitary standard deviation distribution, in preparation for machine learning processing with packages like deepMedic (https://github.com/Kamnitsask/deepmedic).

Let's look below at the code block for step number 3, where we resample to isotropic resolution:

```
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

pipeline.execute('resample', input_files, input_search_phrase, input_exclusion_phrase,
  output_folder, output_suffix, method, extra_parameters)

#--------------------------------------------------------------------#
```

### Input
Every pre-processing method has the same options for input. "input_files" can be either a list of files to process, a list of directories, or both. "input_search_phrase" is an optional regular expression to apply to the directories provided in "input_files". Above, it is set to '\*.nii\*' to only pick up nifti files. "input_exclusion_phrase" is another optional string. Files that includethe string provided to "input_exclusions_phrase" in their filename will not be chosen for pre-processing.

### Output
Similarly, every method has the same options for output. "output_folder" is where the files should be outputted after a pre-processing step is finished. If the provided "output_folder" does not exist, one will be made. "output_suffix" is a label that will be applied at the end of a filepath after it has been pre-processed, in order to keep track of which steps have been performed on it. In this case, a file named "Example.nii.gz" would be labeled "Example_isotropic.nii.gz" after processing.

### Implementation
Each step will have an option called "method." Although there is only one way to do each step currently, there may in the future be multiple software or implementations of the same pre-processing step. Method lets you specify between these packages. Available methods for any pre-processing step should be included in a commented line at the top of the blocl.

### Specific Parameters
The following parameters are extra parameters specific to each pre-processing step. They are collected in the "extra_parameters" variable, and passed to the final command. In this case, one can choose the dimensions to resample each volume to and the interpolation mode for resampling. Documentation on each of these parameters is forthcoming!

### Execute
The final portion is a call to the main pre-processing package, "pipeline", to execute the pre-processing step. The only part of this step that should change from method to method is the first parameter, which is an indicator for which pre-processing step should be performed. Currently, the available indicators are: {'dicom_convert', 'resample', 'bias_correct', 'crop', 'register', 'skull_strip', 'normalize'}

By chaining blocks like these together and keeping track of input/ouput folders and filenames, one can create any number of linear pre-processing pipelines. Currently, the pipeline is only built to process one patient visit at a time. Until support for batch processing of multiple patients/visits is added, however, it should not be difficult to wrap a "pipeline_script.py" script in a loop for each visit you wish to process.

Send any questions or requests for methods to abeers@mgh.harvard.edu. Happy pre-processing!




