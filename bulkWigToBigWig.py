#########################################################################                                              
#                                                                                                                     
# Tess Jeffers                                                                                                        
# January 2016                                                                                                        
#                                                                                                                      
# python script to convert all .wig files in a directory to .bigwig                                                    
# DOES NOT DELETE the .wig file after conversion
#
# requires Jim Kent's UCSC source util's installed globally:                                                          
# https://github.com/ENCODE-DCC/kentUtils                                                                              
# and chromosome_lengths.txt for appropriate ref. assembly                                                             
#                                                                                                                      
# syntax:                                                                                                              
# $ bulkWigToBigWig.py /full/path/to/files/ /full/path/to/chrom_lengths.txt                                       
###########################################################################                                           
import subprocess
import os
import sys

files = os.listdir(sys.argv[1])

for f in files:
   
    extension = f.split(".")

    # check to see if file is .wig type
    if extension[-1] == "wig":
        print("converting " + f + " to bigwig")
        wigFile = sys.argv[1] + f
        bigWigFile = sys.argv[1] + extension[0] + ".bw"
        call = "wigToBigWig " + wigFile + " " + sys.argv[2] + " " + bigWigFile
        print(call)
        subprocess.call([call], shell = True)
    # skip if file is not .wig
    else:
        print("skipping " + f)
