import os
import glob
# import slicer

from optparse import OptionParser

def convert_dicom(input_folder, output_filename):
    
    dicom_files = glob.glob(os.path.join(input_folder, '*'))

    # db = slicer.dicomDatabase

    if slicer.dicomDatabase == None:
        slicer.dicomDatabase = ctk.ctkDICOMDatabase()
        slicer.dicomDatabase.openDatabase(os.path.dirname(os.path.realpath(__file__)) + "Slicer_Dicom_Database/ctkDICOM.sql", "SLICER")
    db = slicer.dicomDatabase

    plugins = [slicer.modules.dicomPlugins['DICOMScalarVolumePlugin'](), slicer.modules.dicomPlugins['DICOMScalarVolumePlugin'](), slicer.modules.dicomPlugins['DICOMScalarVolumePlugin']()]

    for plugin in plugins:
        print plugin
        # try:
        if plugin:
            loadables = plugin.examine([dicom_files])

            if len(loadables) == 0:
                print('plugin failed to interpret this series')
            else:

                patientID = db.fileValue(loadables[0].files[0],'0010,0020')
                seriesDescription = db.fileValue(loadables[0].files[0],'0008,103e')
                seriesDescription = "".join(x for x in seriesDescription if x.isalnum())
                seriesDate = db.fileValue(loadables[0].files[0],'0008,0020')
                seriesTime = db.fileValue(loadables[0].files[0],'0008,0031')
                flipAngle = db.fileValue(loadables[0].files[0],'0018,1314')
                echoTime = db.fileValue(loadables[0].files[0],'0018,0081')
                repTime = db.fileValue(loadables[0].files[0],'0018,0080')

                output_directory = os.path.dirname(output_filename)
                output_filename =  os.path.join(output_directory, patientID + '_' + seriesDescription + '.nii.gz')

                print output_filename
                print os.getcwd()

                volume = plugin.load(loadables[0])
                if volume:
                    slicer.util.saveNode(volume,output_filename)
                    slicer.util.quit()
                    return

        else:
            continue

        # except:
            # continue

    slicer.util.quit()
    return

if __name__ == '__main__':
    parser = OptionParser()
    parser.add_option("-i", "--vol", dest="InputFolder", help="Input DICOM Folder")
    parser.add_option("-o", "--out", dest="OutputNifti", help="Output Nifti Filepath")
    (options, args) = parser.parse_args()
    convert_dicom(options.InputFolder, options.OutputNifti)