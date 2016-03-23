########################################################################
# 
# Tess Jeffers 
# 03.23.2015
#
# goal: batch calculate MD5 checksums on files
# that will be deposited to GEO
#
# syntax: 
# $ python checkMD5.py /full/path/to/files /output/file/with/sums.txt 
######################################################################


import subprocess
import os
import sys

# get list of all files within directory to be submitted to GEO
files = os.listdir(sys.argv[1])

for f in files:

    #print("checking md5 of " + f)
    call = "md5 " + f + ">> " + sys.argv[2]
    
    # print call to screen
    print(call)
    subprocess.call([call], shell = True)
