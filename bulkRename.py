#############################################
### Tess Jeffers
###
### 2.08.2016
### 
### batch rename files downloaded from Galaxy
### syntax: 
### python bulkRename.py /full/path/to/files
#############################################

import sys
import os
import re

def rename_files(directory):

    print("Renaming files in: " +  directory)

    for old_file_name in os.listdir(directory):
        delimited  = re.split('\\[|\\]', old_file_name)

        if len(delimited) > 1:
            print("Renaming: " + old_file_name + " to: " + delimited[1])
            os.rename(os.path.join(directory, old_file_name), os.path.join(directory,delimited[1]))

PATH = os.path.abspath(sys.argv[1])

## main ##
rename_files(PATH)
