# Python 3 code to unzip multiple
# files in a directory or folder

import os, zipfile

# Function to unzip files
def unzip():

    dir_name = r"C:\Users\trong\Downloads\Cyclistic Data"
    extension = ".zip"
    # change directory from working dir to dir with files
    os.chdir(dir_name)

    # loop through items in dir
    for item in os.listdir(dir_name):
        # check for ".zip" extension
        if item.endswith(extension):
            # get full path of files
            file_name = os.path.abspath(item)
            # create zipfile object
            zip_ref = zipfile.ZipFile(file_name)
            listOfFileNames = zip_ref.namelist()
            for fileName in listOfFileNames:
                # check for ".csv" extension inside zip file
                if fileName.endswith(".csv"):
                    # Extract files from zip into a new created folder
                    zip_ref.extract(fileName, "temp_folder")
            # close file
            zip_ref.close()
            print("Extracting files...")
            # delete zipped file
            # os.remove(file_name)


# Calling main() function
unzip()
print("Files extracted!")
