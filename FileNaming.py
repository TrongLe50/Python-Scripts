# Python 3 code to rename multiple
# files in a directory or folder

import os, glob

# Function to rename files
def rename():

    path = r"C:\Users\trong\Downloads\Cyclistic Data\temp_folder\\"
    # search csv files
    pattern = path + "*.csv"
    # List of the files that match the pattern
    result = glob.glob(pattern)

    # Iterating the list with the count
    count = 1
    for file_name in result:
        old_name = file_name
        new_name = path + "CyclisticData_" + str(count) + ".csv"
        os.rename(old_name, new_name)
        count = count + 1


# Calling main() function
rename()
print("All Files Renamed")
